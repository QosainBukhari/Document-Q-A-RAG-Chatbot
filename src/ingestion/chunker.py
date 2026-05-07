import yaml

from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.utils.logger import logger


class TextChunker:

    def __init__(self,
                 config_path="configs/config.yaml"):

        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        self.chunk_size = config["chunk_size"]
        self.chunk_overlap = config["chunk_overlap"]

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def create_chunks(self, documents):

        try:
            chunks = self.text_splitter.split_documents(
                documents
            )

            logger.info(
                f"Created {len(chunks)} chunks"
            )

            return chunks

        except Exception as e:
            logger.error(f"Chunking failed: {e}")
            raise