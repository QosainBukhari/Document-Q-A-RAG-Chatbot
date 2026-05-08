from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.chunker import TextChunker
from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.chroma_store import ChromaVectorStore

# Load PDF
loader = PDFLoader("data/raw/Ml_book.pdf")
text = loader.load_pdf()

# Create chunks
chunker = TextChunker()
chunks = chunker.create_chunks(text)

# Load embedding model
embedding_model = EmbeddingModel().get_model()

# Create vector DB
vectordb = ChromaVectorStore(
    embedding_model
).create_vector_store(chunks)

print("Vector DB created successfully")