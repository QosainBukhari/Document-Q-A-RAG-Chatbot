from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.chroma_store import ChromaVectorStore
from src.retriever.retriever import Retriever

# Load embedding model
embedding_model = EmbeddingModel().get_model()

# Load existing DB
vectordb = ChromaVectorStore(
    embedding_model
).load_vector_store()

# Create retriever
retriever = Retriever(vectordb)

query = "What is the self attention?"

results = retriever.retrieve(query)

for i, doc in enumerate(results, start=1):

    print(f"\nRESULT {i}\n")

    print(doc.page_content[:500])