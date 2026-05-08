from src.utils.logger import logger


class RAGChain:

    def __init__(
        self,
        retriever,
        llm,
        memory=None
    ):

        self.retriever = retriever
        self.llm = llm
        self.memory = memory

    def generate_answer(self, query: str):

        try:

            # Retrieve relevant chunks
            retrieved_docs = self.retriever.retrieve(query)

            # Handle empty retrieval
            if not retrieved_docs:

                logger.warning(
                    "No relevant documents retrieved"
                )

                return {
                    "question": query,
                    "answer": (
                        "I don't know based on the document."
                    ),
                    "sources": []
                }

            # Load conversation history
            history_text = ""

            if self.memory:

                history_text = (
                    self.memory.get_history()
                )

            # Build formatted context
            context = "\n\n".join([
                f"""
Source: {doc.metadata.get("source", "Unknown")}
Page: {doc.metadata.get("page", "N/A")}

Content:
{doc.page_content}
"""
                for doc in retrieved_docs
            ])

            prompt = f"""
You are an intelligent Retrieval-Augmented Generation (RAG) assistant.

Your task is to answer the user's question using ONLY the provided context.

Instructions:
- Do NOT use outside knowledge.
- If the answer is not available in the context, respond exactly with:
  "I don't know based on the document."
- Provide clear, accurate, and well-structured answers.
- Explain technical concepts in simple language.
- Include important definitions, examples, formulas, or key points when available.
- Use chat history only for conversational continuity.
- Avoid repeating information.
- Keep the response professional and concise.
- Mention source page numbers naturally when relevant.

Chat History:
---------------------
{history_text}
---------------------

Context:
---------------------
{context}
---------------------

Question:
{query}

Answer:
"""

            # Generate response
            response = self.llm.invoke(prompt)

            # Handle response format
            answer = (
                response.content
                if hasattr(response, "content")
                else str(response)
            )

            # Save conversation
            if self.memory:

                self.memory.save_context(
                    query,
                    answer
                )

            logger.info(
                "Generated RAG response successfully"
            )

            # Clean unique sources
            sources = []

            for doc in retrieved_docs:

                source_info = {
                    "source": doc.metadata.get(
                        "source",
                        "Unknown"
                    ),
                    "page": doc.metadata.get(
                        "page",
                        "N/A"
                    )
                }

                if source_info not in sources:

                    sources.append(source_info)

            return {
                "question": query,
                "answer": answer,
                "sources": sources
            }

        except Exception as e:

            logger.error(
                f"RAG chain failed: {e}"
            )

            raise