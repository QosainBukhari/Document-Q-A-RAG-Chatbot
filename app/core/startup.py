from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.chroma_store import ChromaVectorStore
from src.llm.ollama_client import OllamaClient

from src.utils.logger import logger


def load_models(app):

    try:
        logger.info("Loading embedding model...")

        embedding_model = EmbeddingModel().get_model()

        logger.info("Loading vector database...")

        vectordb = ChromaVectorStore(
            embedding_model
        ).load_vector_store()

        logger.info("Loading LLM...")

        llm = OllamaClient().get_llm()

        # Store globally inside FastAPI app
        app.state.embedding_model = embedding_model
        app.state.vectordb = vectordb
        app.state.llm = llm

        logger.info("All models loaded successfully")

    except Exception as e:

        logger.error(f"Startup loading failed: {e}")

        raise