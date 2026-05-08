import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

from src.utils.logger import logger

load_dotenv()


class EmbeddingModel:
    def __init__(self):

        self.model_name = os.getenv(
                "EMBEDDING_MODEL",
                "all-MiniLM-L6-v2"
            )

        try:
            self.embedding_model = HuggingFaceEmbeddings(
                model_name=self.model_name
            )

            logger.info(
                f"Embedding model loaded: {self.model_name}"
            )

        except Exception as e:
            logger.error(f"Failed to load embedding model: {e}")
            raise

    def get_model(self):

        return self.embedding_model