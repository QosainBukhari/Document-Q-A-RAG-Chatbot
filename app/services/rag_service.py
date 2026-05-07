from src.retriever.retriever import Retriever
from src.llm.rag_chain import RAGChain


class RAGService:

    def __init__(self, vectordb, llm):

        self.retriever = Retriever(vectordb)

        self.rag_chain = RAGChain(
            self.retriever,
            llm
        )

    def ask_question(self, question: str):

        response = self.rag_chain.generate_answer(
            question
        )

        return response