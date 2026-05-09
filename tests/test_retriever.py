from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.chunker import TextChunker

from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.chroma_store import ChromaVectorStore
from src.retriever.retriever import Retriever


def test_retriever():

    loader = PDFLoader(
        "test/Ml_book.pdf"
    )

    documents = loader.load_pdf()

    chunker = TextChunker()

    chunks = chunker.create_chunks(
        documents
    )

    embedding_model = (
        EmbeddingModel().get_model()
    )

    vectordb = ChromaVectorStore(
        embedding_model
    ).create_vector_store(chunks)

    retriever = Retriever(vectordb)

    results = retriever.retrieve(
        "What is this document about?"
    )

    assert results is not None

    assert len(results) > 0