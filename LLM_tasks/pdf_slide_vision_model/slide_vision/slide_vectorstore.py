import os
import logging
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from dotenv import load_dotenv
import sys
import numpy as np
import requests
from io import BytesIO
from PIL import Image
import faiss
import pytesseract

# --> Setup django for standalone use
# sys.path.append('/Users/mahima/Documents/daphne-academy/academy-brain')
# sys.path.append('/Users/mahima/Documents/daphne-academy/academy-brain/academy_assistant')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academy.settings')

from academy_assistant.database.graphql import GraphqlClient

class SlideIndexer:
    def __init__(self, text_dir, output_dir='slide_vector_store'):
        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_dir_slide_text = os.path.join(current_file_dir, "processed_slides")
        os.makedirs(self.output_dir_slide_text, exist_ok=True)

        self.text_dir = text_dir
        self.output_dir = os.path.join(current_file_dir,output_dir)
        self.documents = []
        
        # Initialize OpenAIEmbeddings
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-ada-002" 
        )
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Create the output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def extract_text_from_image(self, image_url, module_name, slide_number):
        text = ""
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img_text = pytesseract.image_to_string(img)
        text += "\n" + img_text
        # Save extracted text
        with open(f"{self.output_dir_slide_text}/{module_name}_slide_{slide_number+1}.txt", "w") as f:
            f.write(f"Module Name: {module_name}\n")
            f.write(f"Slide Number: {slide_number+1}\n\n")
            f.write(f"Main Content:\n{text}")

    def normalize_embeddings(embeddings):
        """Normalize embeddings to unit length."""
        norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
        return embeddings / norms

    def load_texts(self):
        for file_name in os.listdir(self.text_dir):
            if file_name.endswith('.txt'):
                file_path = os.path.join(self.text_dir, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    # Extract metadata from file name if needed
                    parts = file_name.replace(".txt", "").split("_slide_")
                    module_name, slide_number = parts[0].replace("_", " "), int(parts[1])
                    metadata = {
                        "file_name": file_name,
                        "module_name": module_name,
                        "slide_number": slide_number
                    }
                    doc = Document(page_content=content, metadata=metadata)
                    self.documents.append(doc)
                    self.logger.info(f"Loaded {file_name} {module_name} {slide_number}")
                except Exception as e:
                    self.logger.error(f"Failed to load {file_name}: {str(e)}")

    # def create_faiss_store(self):
    #     if not self.documents:
    #         self.logger.warning("No documents to index. Ensure text files are loaded.")
    #         return
        
    #     try:
    #         vector_store = FAISS.from_documents(self.documents, self.embeddings)
    #         vector_store.save_local(self.output_dir)
    #         self.logger.info(f"SLide vector store created and saved at '{self.output_dir}/'")
    #     except Exception as e:
    #         self.logger.error(f"Failed to create vector store: {str(e)}")

    def create_faiss_store(self):
        if not self.documents:
            self.logger.warning("No documents to index. Ensure text files are loaded.")
            return
        
        try:
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
            vectorstore.save_local(self.output_dir)
            self.logger.info(f"SLide vector store created and saved at '{self.output_dir}/'")
        except Exception as e:
            self.logger.error(f"Failed to create vector store: {str(e)}")

if __name__ == "__main__":
    # load_dotenv()  # Load environment variables from .env if available
    db_client = GraphqlClient(None)
    modules = db_client.get_learning_modules()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    text_directory = os.path.join(BASE_DIR, 'processed_slides')
    indexer = SlideIndexer(text_directory)

    # Uncomment the below code when new slides are added to the database

    # for module in modules:
    #     for num in range(len(module['slides'])):
    #         if module['slides'][num]['type'] == 'info':
    #             imageurl_info = db_client.get_slide_info(module["id"],num)
    #             slide_image = imageurl_info[0]['image_url']
    #             file_name = f"{module['name']}_slide_{num+1}"
    #             indexer.extract_text_from_image(slide_image, module['name'], num)

    # indexer.load_texts()
    # indexer.create_faiss_store()
    print("Slides vector store created successfully.")
