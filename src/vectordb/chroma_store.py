import os

from dotenv import load_dotenv
from langchain_chroma import Chroma

from src.utils.logger import logger

load_dotenv()


class ChromaVectorStore:

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model

        self.persist_directory = os.getenv("CHROMA_DB_DIR")

    def create_vector_store(self, chunks):

        try:

            valid_chunks = []

            for chunk in chunks:

                try:
                    # Extract content safely
                    content = getattr(chunk, "page_content", None)

                    # Skip invalid content
                    if not isinstance(content, str):
                        continue

                    # Clean text
                    content = (
                        content.encode(
                            "utf-8",
                            errors="ignore"
                        )
                        .decode("utf-8")
                        .strip()
                    )

                    # Skip tiny/empty chunks
                    if len(content) < 20:
                        continue

                    # Update cleaned content
                    chunk.page_content = content

                    # Ensure metadata exists
                    if not hasattr(chunk, "metadata"):
                        chunk.metadata = {}

                    valid_chunks.append(chunk)

                except Exception as chunk_error:

                    logger.warning(
                        f"Skipping malformed chunk: {chunk_error}"
                    )

                    continue

            if not valid_chunks:
                raise ValueError(
                    "No valid chunks available for vector DB creation"
                )

            vectordb = Chroma.from_documents(
                documents=valid_chunks,
                embedding=self.embedding_model,
                persist_directory=self.persist_directory
            )

            logger.info(
                f"Stored {len(valid_chunks)} chunks in ChromaDB"
            )

            return vectordb

        except Exception as e:

            logger.error(f"Failed to create vector DB: {e}")

            raise

    def load_vector_store(self):

        try:

            vectordb = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embedding_model
            )

            logger.info("ChromaDB loaded successfully")

            return vectordb

        except Exception as e:

            logger.error(f"Failed to load ChromaDB: {e}")

            raise