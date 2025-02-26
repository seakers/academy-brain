import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract
import requests
import pickle
import sys
import tempfile
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from rank_bm25 import BM25Okapi
import numpy as np
import faiss 

# --> Setup django for standalone use
# sys.path.append('/Users/mahima/Documents/daphne-academy/academy-brain')
# sys.path.append('/Users/mahima/Documents/daphne-academy/academy-brain/academy_assistant')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academy.settings')

from academy_assistant.database.graphql import GraphqlClient

class PDFIndexer:
    def __init__(self, text_output_dir='extracted_pdf_texts'):
        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        self.text_output_dir = os.path.join(current_file_dir,text_output_dir)
        self.documents = []
        
        self.embeddings = OpenAIEmbeddings()
        os.makedirs(self.text_output_dir, exist_ok=True)

    def load_documents_from_folder(self, folder_path):
        documents = []
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "r") as file:
                    text = file.read()
                    chunks = text_splitter.split_text(text)
                    for chunk in chunks:
                        chunk_metadata = {"filename": filename, "chunk_start": chunk[:50]}
                        doc = Document(page_content=chunk, metadata=chunk_metadata)
                        documents.append(doc)
        return documents
    
    def normalize_embeddings(embeddings):
        """Normalize embeddings to unit length."""
        norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
        return embeddings / norms

    def extract_text_from_pdf(self, url, title):
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to download PDF from {url}")
            return None

        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp.write(response.content)
            tmp.flush()
            pdf_path = tmp.name
            
        reader = PdfReader(pdf_path)
        num_pages = len(reader.pages)
        full_text = ""

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text() or ""

            images = convert_from_path(pdf_path, first_page=page_num+1, last_page=page_num+1, dpi=300)
            if images:
                image = images[0]
                ocr_text = pytesseract.image_to_string(image)
                text += "\n" + ocr_text

            metadata = {
                "textbook_name": title,
                "source": pdf_path,
                "page_number": page_num + 1
            }
            self.store_text_with_metadata(text, metadata)
            full_text += text

        return full_text
    
    def store_text_with_metadata(self, text, metadata):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_text(text)

        for chunk in chunks:
            chunk_metadata = metadata.copy()
            chunk_metadata["chunk_start"] = chunk[:50]  # Add a snippet of the chunk start for reference
            doc = Document(page_content=chunk, metadata=chunk_metadata)
            self.documents.append(doc)

    def process_pdfs(self, url, title):
        # Extract text from PDF
        text = self.extract_text_from_pdf(url, title)
        text_file_path = os.path.join(self.text_output_dir, f"{title}.txt")
        try:
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
            print(f"Saved extracted text to {text_file_path}")
        except Exception as e:
            print(f"Failed to save text for {title}: {str(e)}")

    # def create_vector_store(self):
    #     vector_store = FAISS.from_documents(self.documents, self.embeddings)
    #     vector_store.save_local("pdf_vector_store")
    #     print("Vector store created and saved locally.")

    def create_vector_store(self):
        # Generate embeddings for all documents
        embeddings_list = [self.embeddings.embed_query(doc.page_content) for doc in self.documents]
        
        # Normalize the embeddings
        normalized_embeddings = self.normalize_embeddings(np.array(embeddings_list))
        
        # Create FAISS index with Inner Product (IP)
        dimension = normalized_embeddings.shape[1]
        faiss_index = faiss.IndexFlatIP(dimension)
        faiss_index.add(normalized_embeddings)
        
        # Create FAISS vectorstore from the index
        vectorstore = FAISS(self.embeddings,index=faiss_index)
        vectorstore.save_local("pdf_vector_store")
        print("Vector store created and saved locally.")
        

    def create_bm25_index(self, documents):
        tokenized_corpus = [doc.page_content.split() for doc in self.documents]
        bm25 = BM25Okapi(tokenized_corpus)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        bm25_index_path = os.path.join(script_dir, "bm25_index.pkl")
        with open(bm25_index_path, "wb") as f:
            pickle.dump(bm25, f)
        self.bm25 = bm25
        print("BM25 index created and saved locally.")
        return bm25
    
    def save_embedded_documents_to_pkl(self, pkl_path):
        with open(pkl_path, "wb") as f:
            pickle.dump(self.documents, f)
        print(f"Documents saved to {pkl_path}")
    
    def save_documents_to_pkl(self, documents, pkl_path):
        with open(pkl_path, "wb") as f:
            pickle.dump(documents, f)
        print(f"Documents saved to {pkl_path}")

    def add_new_pdf(self, url, title):
        """
        Process a new PDF file given its URL and title:
        1. Extract text from the PDF.
        2. Split the text into chunks (if your use-case requires segmentation).
        3. Create Document objects with metadata.
        4. Load the existing FAISS vector store.
        5. Add the new documents to the index and save it locally.
        """
        # Extract text from the new PDF file
        text = self.process_pdfs(url, title)
        if not text:
            print(f"Failed to extract text from PDF: {title}")
            return
        
        # Load the existing FAISS vector store.
        # Ensure self.embeddings is properly defined in your PDFIndexer class.
        try:
            vector_store = FAISS.load_local("pdf_vector_store", self.embeddings)
        except Exception as e:
            print(f"Failed loading FAISS index: {e}")
            return

        # Add new documents and update the index.
        vector_store.add_documents(self.documents)
        vector_store.save_local("pdf_vector_store")
        print(f"Added new PDF '{title}' to the vector store.")

if __name__ == "__main__":

    db_client = GraphqlClient(None)
    textbooks = db_client.get_textbooks()
    indexer = PDFIndexer()


    # Uncomment the below code when new PDFs are added to the database

    # for textbook in textbooks:
    #     print("textbook",textbook["title"], textbook["textbook_url"])
    #     indexer.process_pdfs(textbook['textbook_url'], textbook['title'])

    # indexer.create_vector_store()

    # Comment the above code and uncomment the below code to add a new PDF
    
    # indexer.add_new_pdf(url, title)

    print("Pdf vector store created")

    