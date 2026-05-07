import os

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

from src.utils.logger import logger

load_dotenv()


class OllamaClient:

    def __init__(self):

        self.model = os.getenv("OLLAMA_MODEL")
        self.base_url = os.getenv("OLLAMA_BASE_URL")

        try:
            self.llm = OllamaLLM(
                model=self.model,
                base_url=self.base_url
            )

            logger.info(
                f"Ollama model loaded: {self.model}"
            )

        except Exception as e:
            logger.error(f"Failed to connect Ollama: {e}")
            raise

    def get_llm(self):

        return self.llm