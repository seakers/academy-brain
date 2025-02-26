import re
from typing import TypedDict, Annotated, Sequence, List, Dict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langgraph.graph import END, StateGraph, START
import json
from langchain_core.runnables.graph import MermaidDrawMethod
from sentence_transformers import SentenceTransformer, util
from collections import deque
import pickle
import os

class AgentState(TypedDict):
    messages: Sequence[BaseMessage]
    current_slide: int
    current_module: str
    current_slide_data: List[Dict]
    slides_context: List[Dict]
    pdf_context: List[Dict]
    reflection: Dict
    final_answer: str
    citation_metadata: Dict
    conversation_history: List[Dict]
    relevant_history: List[Dict]

CONVERSATION_MEMORY_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Review the conversation history and current question.
    Identify relevant past exchanges that could help answer the current question. If no history, return an empty list.
    Return past exchanges that provide useful context."""),
    ("user", """Conversation History: {history}
    Current Question: {question}""")
])

# QUERY_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages([
#     ("system", """Analyze the question considering the conversation history.
#     Determine complexity and required depth.
#     Consider previous related questions and answers."""),
#     ("user", """Conversation History: {history}
#     Current Question: {question}
#     Current Slide: {current_slide}""")
# ])

QUERY_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Analyze the question and classify it into one of the following categories:
    1. 'current_slide' - if the question is about the current slide.
    2. ‘general_slides’ - if the question is not about the current slide or if the question is about the slides in general, go here unless asked to explain or asked again about a topic.
    3. 'complex' - if the user asks for deeper explanation about a previously asked question.
    4. 'general' - if the question is a general question like a greeting. 
    Return only a word from current_slide, general_slides, complex, general indicating the category.

    Consider previous related questions and answers.
    """),
        ("user", """Conversation History: {history}
    Current Question: {question}
    Current Slide: {current_slide}
    Current Slide Data: {current_slide_data}""")
])

ANSWER_GENERATION_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are a precise teaching assistant. Use the given context and conversation history.
    Always cite sources and BE SURE TO CITE the MODULE NAME, SLIDE NUMBER or TEXTBOOK NAME AND FORMAT citations as [Module X Slide Y] or [Textbook Z].
    Use only this notation for citing:
    - For slides: [Module Name - Slide Y] (example: [Orbital Mechanics - Slide 4])
    - For textbooks: [Textbook: Book Name - Page Page Number] (example: [Textbook: GRIFFIN-Space Vehicle Design - Page 2])
    Combine multiple sources coherently.
    If no relevant context is provided, answer the question to the best of your ability."""),
    ("user", """Slides Context: {slides_context}
    PDF Context: {pdf_context}
    Question: {question}
    Previous Reflection: {reflection}
    Relevant History: {relevant_history}""")
])

REFLECTION_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """Evaluate the answer quality and completeness based on the following criteria:
    1. Question fully addressed
    2. Accurate citations
    3. Clear explanations
    4. Need for additional context
    5. Consistency with previous answers
    
    Give the json object consisting of quality_score, needs_improvement flag, missing_aspects, suggested_sources, and consistency_check.
    Rate the quality_score on 10. If needs_improvement is True, provide missing_aspects and suggested_sources.
    """),
        ("user", """Question: {question}
    Answer: {answer}""")
])

GENERAL_ANSWER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful teaching assistant. For general questions, provide friendly and informative responses.
    If the question is a greeting or general inquiry, respond appropriately.
    If the question is about the course but without specific context, provide a high-level response."""),
    ("user", "{question}")
])


class AdaptiveRAG:
    def __init__(self, slides_path: str, pdfs_path: str):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.2)
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-ada-002"
        )
        self.slides_vectorstore = FAISS.load_local(
            slides_path,
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True  # Only use with trusted files
        )
        self.pdfs_vectorstore = FAISS.load_local(
            pdfs_path,
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True  # Only use with trusted files
        )
        # self.memory = ConversationBufferMemory(return_messages=True)
        self.workflow = self._build_workflow()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # bm25_index_path = os.path.join(script_dir, "pdf_vision", "bm25_index.pkl")
        # with open(bm25_index_path, "rb") as f:
        #     self.bm25_index = pickle.load(f)
        # self.semantic_model = SentenceTransformer('all-MiniLM-L6-v2')
        # documents_path = os.path.join(script_dir, "pdf_vision", "documents.pkl")
        # self.documents = self.load_documents(documents_path)

    def load_documents(self, documents_path):
        with open(documents_path, "rb") as f:
            documents = pickle.load(f)
        return documents
    

    def reciprocal_rank_fusion(faiss_results, bm25_results, k):
        combined_scores = {}
        for rank, doc_id in enumerate(faiss_results):
            combined_scores[doc_id] = combined_scores.get(doc_id, 0) + 1 / (rank + 1)
        for rank, doc_id in enumerate(bm25_results):
            combined_scores[doc_id] = combined_scores.get(doc_id, 0) + 1 / (rank + 1)
        sorted_combined = sorted(combined_scores.items(), key=lambda item: item[1], reverse=True)
        return [doc_id for doc_id, score in sorted_combined[:k]]

    # def semantic_ranker(self, query, documents):
    #     query_embedding = self.semantic_model.encode(query, convert_to_tensor=True)
    #     doc_embeddings = self.semantic_model.encode(documents, convert_to_tensor=True)
    #     scores = util.pytorch_cos_sim(query_embedding, doc_embeddings)[0]
    #     ranked_docs = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)
    #     return [doc for doc, score in ranked_docs]

    def _get_relevant_history(self, state: Dict) -> Dict:
        """Identify relevant past exchanges"""
        history = state["conversation_history"]
    
        current_question = state["messages"][-1].content
        
        response = self.llm.invoke(
            CONVERSATION_MEMORY_PROMPT.format(
                history=history,
                question=current_question
            )
        )
        print("-------------Getting releveant history---------------\n", response.content)
        
        return {"relevant_history": json.loads(response.content)}

    def _query_understanding(self, state: Dict) -> Dict:
        """Analyze query and classify the question"""
        question = state["messages"][-1].content
        history = state["conversation_history"]
        print("relevant history",history)
        
        response = self.llm.invoke(
            QUERY_ANALYSIS_PROMPT.format(
                history=(history),
                question=question,
                current_slide=state["current_slide"],
                current_slide_data=state["current_slide_data"]
            )
        )
        print("-------------Query Analysis---------------\n", response.content)
        return {"query_analysis": response.content}
    
    def _search_current_slide(self, state: Dict) -> Dict:
        """Search only the current slide"""
        query = state["messages"][-1].content
        current_slide = state["current_slide"]
        current_module = state["current_module"]
        
        docs = self.slides_vectorstore.similarity_search(
            query,
            k=1,
            filter={
                "slide_number": current_slide,
                "module_name": current_module
                }
        )
        print("-------------Searching Current Slide---------------\n", current_slide, current_module,docs)
        
        return {
            "slides_context": [{
                "content": doc.page_content,
                "metadata": doc.metadata
            } for doc in docs]
        }

    def _search_all_slides(self, state: Dict) -> Dict:
        """Search slides with context window"""
        query = state["messages"][-1].content
        docs = self.slides_vectorstore.similarity_search(query, k=8)
        print("-------------Searching all slides---------------\n", docs)
    
        return {
            "slides_context": [{
                "content": doc.page_content,
                "metadata": doc.metadata
            } for doc in docs]
        }

    def _search_pdfs(self, state: Dict) -> Dict:
        """Search PDFs with historical context"""
        query = state["messages"][-1].content
        history_context = state["conversation_history"]
        enhanced_query = f"{query} {history_context}"

        # query_vector = self.semantic_model.encode(enhanced_query, convert_to_tensor=True).numpy()
        docs = self.pdfs_vectorstore.similarity_search(enhanced_query, k=5)
        # tokenized_query = enhanced_query.split(" ")
        # bm25_results = self.bm25_index.get_top_n(tokenized_query, [doc.page_content for doc in self.documents], n=5)
        # print("--------------------------------------------\n", faiss_results)
        # print("----------------------------------------------------------")
        # print(bm25_results)
        # print("----------------------------------------------------------")
        # documents = self.reciprocal_rank_fusion(faiss_results, bm25_results, 5)
        # documents = [self.retrieve_document(doc_id) for doc_id in combined_results]
        # ranked_documents = self.semantic_ranker(enhanced_query, documents)
        
        # docs = self.pdfs_vectorstore.similarity_search(
        #     enhanced_query,
        #     k=3
        # )
        print("-------------Searching pdfs---------------\n", docs)
        
        return {
            "pdf_context": [{
                "content": doc.page_content,
                "metadata": doc.metadata
            } for doc in docs]
        }
    
    def _generate_general_answer(self, state: Dict) -> Dict:
        """Generate answer for general questions not related to slides or PDFs"""
        question = state["messages"][-1].content
        
        # Format the prompt using GENERAL_ANSWER_PROMPT
        prompt = GENERAL_ANSWER_PROMPT.format(question=question)
        
        # Invoke the LLM with the formatted prompt
        response = self.llm.invoke(prompt)
        
        print("-------------General Answer---------------")
        print(response.content)
        
        return {
            "messages": [*state["messages"], AIMessage(content=response.content)],
            "final_answer": response.content,
            "conversation_history": [*state["conversation_history"], {
                "role": "assistant",
                "content": response.content
            }]
        }

    def _generate_answer(self, state: Dict) -> Dict:
        """Generate answer considering possible empty contexts"""
        slides_context = state.get("slides_context", [])
        pdf_context = state.get("pdf_context", [])
        relevant_history = state.get("conversation_history", [])

        slides_text = "\n".join([
            f"[{doc['metadata']['module_name']} Slide {doc['metadata']['slide_number']}] {doc['content']}"
            for doc in slides_context
        ]) if slides_context else ""

        print("----------------------------------------------")
        for doc in pdf_context:
            print(doc['metadata'])
        print("----------------------------------------------")


        pdf_text = "\n".join([
            f"[Textbook: {doc['metadata']['textbook_name']} - Page {doc['metadata']['page_number']}] {doc['content']}"
            for doc in pdf_context
        ]) if pdf_context else ""

        # history_text = "\n".join([
        #     f"[Previous Discussion] {h['content']}"
        #     for h in relevant_history
        # ]) if relevant_history else ""
        print("----------------> Relevant history", relevant_history)

        response = self.llm.invoke(
            ANSWER_GENERATION_PROMPT.format(
                slides_context=slides_text,
                pdf_context=pdf_text,
                question=state["messages"][-1].content,
                reflection=json.dumps(state.get("reflection", {})),
                relevant_history=relevant_history
            )
        )

        print("-------------Generating answer---------------\n", response.content)

        return {
            "messages": [*state["messages"], AIMessage(content=response.content)],
            "final_answer": response.content,
            "conversation_history": [*state["conversation_history"], {
                "role": "assistant",
                "content": response.content
            }]
        }

    def _reflect(self, state: Dict) -> Dict:
        """Evaluate with historical context"""
        try:
            print("-------------Reflecting---------------")
            print(state["messages"][-2].content)
            print("00000000000000000")
            print(state["final_answer"])
            reflection = self.llm.invoke(
                REFLECTION_PROMPT.format(
                    question=state["messages"][-2].content,
                    answer=state["final_answer"],
                    # history=json.dumps(state.get("conversation_history", []))
                )
            )            
            print("-------------Reflection---------------")
            print(reflection.content)
            
            # Parse JSON response
            # reflection_data = json.loads(reflection.content)
            print("Reflection data: ", reflection.content)
            print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            raw_response = reflection.content.strip()
            json_text = re.sub(r"```json\s*(.*?)```", r"\1", raw_response, flags=re.DOTALL).strip()
            print("json_text", json_text)
            reflection_data = json.loads(json_text)
            print("rrrrrrrrrrrrr", reflection_data)
            
            # # Ensure required fields
            reflection_data.setdefault("quality_score", 7)
            reflection_data.setdefault("needs_improvement", False)
            # reflection_data.setdefault("missing_aspects", [])
            # reflection_data.setdefault("suggested_sources", [])
            # reflection_data.setdefault("consistency_check", {
            #     "consistent": True,
            #     "conflicts": []
            # })
            
            return {"reflection": {"quality_score": 7, "needs_improvement": False, "missing_aspects": [], "suggested_sources": [], "consistency_check": {"consistent": True, "conflicts": []}}}
            
        except Exception as e:
            print(f"Reflection error: {str(e)}")
            # Return default reflection data
            return {
                "reflection": {
                    "quality_score": 7,
                    "needs_improvement": False,
                    "missing_aspects": [],
                    "suggested_sources": [],
                    "consistency_check": {
                        "consistent": True,
                        "conflicts": []
                    }
                }
            }
    def _router(self, state: Dict) -> str:
        """Route based on query analysis"""
        question_type = state["query_analysis"]
        reflection = state.get("reflection", {})
        quality_score = reflection.get("quality_score", 10)
        needs_improvement = reflection.get("needs_improvement", False)

        print("-------------Router---------------\n", question_type)
        
        if question_type == "current_slide":
            return "search_current_slide"
        elif question_type == "general_slides":
            return "search_all_slides"
        elif question_type == "complex":
            return "search_pdfs"
        elif question_type == "general":
            return "generate_general_answer"
        
        # Default behavior
        return "search_all_slides"
    
    def _router_after_reflection(self, state: Dict) -> str:
        """Decide next step after reflection"""
        reflection = state["reflection"]

        print("-------------Router after reflection---------------\n", reflection)
        if reflection["needs_improvement"]:
            suggested_source = reflection.get("suggested_sources", [])
            if "pdf" in suggested_source:
                return "search_pdfs"
        return "end"
    

    # def _router(self, state: Dict) -> str:
    #     """Route based on reflection and history"""
    #     reflection = state["reflection"]
        
    #     if reflection["quality_score"] < 7:
    #         if "history" in reflection["suggested_sources"]:
    #             return "get_relevant_history"
    #         elif "pdf" in reflection["suggested_sources"]:
    #             return "search_pdfs"
    #         return "search_slides"
        
    #     if not reflection["consistency_check"]["consistent"]:
    #         return "generate_answer"
        
    #     return "end"

    def _build_workflow(self) -> StateGraph:
        """Build workflow with history handling"""
        workflow = StateGraph(AgentState)

        workflow.add_node("get_relevant_history", self._get_relevant_history)
        workflow.add_node("query_understanding", self._query_understanding)
        workflow.add_node("search_current_slide", self._search_current_slide)
        workflow.add_node("search_all_slides", self._search_all_slides)
        workflow.add_node("search_pdfs", self._search_pdfs)
        workflow.add_node("generate_answer", self._generate_answer)
        workflow.add_node("generate_general_answer", self._generate_general_answer)
        workflow.add_node("reflect", self._reflect)

        workflow.add_edge(START, "query_understanding")


        workflow.add_edge("get_relevant_history", "query_understanding")
        workflow.add_conditional_edges(
            "query_understanding",
            self._router,
            {
                "search_current_slide": "search_current_slide",
                "search_all_slides": "search_all_slides",
                "search_pdfs": "search_pdfs",
                "generate_general_answer": "generate_general_answer"
            }
        )
        workflow.add_edge("search_current_slide", "generate_answer")
        workflow.add_edge("search_all_slides", "search_pdfs")
        workflow.add_edge("search_pdfs", "generate_answer")
        workflow.add_edge("generate_answer", "reflect")

        workflow.add_conditional_edges(
            "reflect",
            self._router_after_reflection,
            {
                "search_pdfs": "search_pdfs",
                "end": END
            }
        )
        # For general answers, no need to reflect
        workflow.add_edge("generate_general_answer", END)

        return workflow.compile()

    def query(self, question: str, current_module: str, current_slide: int, conversation_history, current_slide_data) -> str:
        """Process question with conversation history"""
        result = self.workflow.invoke({
            "messages": [HumanMessage(content=question)],
            "current_slide": current_slide,
            "current_module": current_module,
            "current_slide_data": current_slide_data,
            "slides_context": [],
            "pdf_context": [],
            "reflection": {},
            "final_answer": "",
            "citation_metadata": {},
            "conversation_history": conversation_history,
            "relevant_history": []
        })
        
        return result["final_answer"]
    
    def display_graph(self) -> None:
        """Generate and save the graph as an image"""
        graph_image_path = "graph.png"
        with open(graph_image_path, "wb") as f:
            f.write(self.workflow.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.API))
        
        print(f"Graph saved as {graph_image_path}. Open it in an image viewer.")

if __name__ == "__main__":
    # Initialize the RAG system
    # rag = AdaptiveRAG(
    #     slides_path="/Users/mahima/Documents/ppt-to-text/slide_vector_store",
    #     pdfs_path="/Users/mahima/Documents/ppt-to-text/pdf_vector_store"
    # )
    base_dir = os.path.dirname(os.path.abspath(__file__))
    rag = AdaptiveRAG(
        slides_path=os.path.join(base_dir, "slide_vision", "slide_vector_store"),
        pdfs_path=os.path.join(base_dir, "pdf_vision", "pdf_vector_store")
    )


    # rag.display_graph()
    # Simulate a conversation
    current_slide = 117
    current_module = "Spacecraft Technologies and Architectures"
    
    

    questions = [
        "What are the typical functions in flight software?",  # Current slide question
        "Can you explain that in more detail?",  # General slides question
        # "Explain about antenna gain in more detail.",  # Complex question
        # "Hi, how are you doing today?"  # General question
    ]

    for question in questions:
        docs = rag.slides_vectorstore.similarity_search(
            question,
            k=1,
            filter={
                "slide_number": current_slide,
                "module_name": current_module
                }
        )
        print("-------------Searching Current Slide---------------\n", current_slide, current_module)
        current_slide_data = [{
                "content": doc.page_content,
                "metadata": doc.metadata
            } for doc in docs]
        answer = rag.query(question, current_module, current_slide, current_slide_data)
        print(f"Question: {question}")
        print(f"Final Answer: {answer}\n")