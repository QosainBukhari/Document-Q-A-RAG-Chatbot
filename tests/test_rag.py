from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.chroma_store import ChromaVectorStore
from src.retriever.retriever import Retriever
from src.llm.ollama_client import GroqClient
from src.llm.rag_chain import RAGChain

# Load embedding model
embedding_model = EmbeddingModel().get_model()

# Load vector DB
vectordb = ChromaVectorStore(
    embedding_model
).load_vector_store()

# Retriever
retriever = Retriever(vectordb)

# LLM
llm = GroqClient().get_llm()

# RAG chain
rag = RAGChain(retriever, llm)

query = "What is self-attention?"

response = rag.generate_answer(query)

print("\nANSWER:\n")
print(response["answer"])

print("\nSOURCES:\n")
print(response["sources"])