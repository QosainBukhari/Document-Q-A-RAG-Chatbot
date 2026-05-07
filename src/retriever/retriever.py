import yaml

from src.utils.logger import logger


class Retriever:

    def __init__(self, vectordb, config_path="configs/config.yaml"):

        self.vectordb = vectordb

        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        self.top_k = config["retriever"]["top_k"]

    def retrieve(self, query: str):

        try:
            results = self.vectordb.similarity_search(
                query,
                k=self.top_k
            )

            logger.info(
                f"Retrieved {len(results)} relevant chunks"
            )

            return results

        except Exception as e:
            logger.error(f"Retrieval failed: {e}")
            raise