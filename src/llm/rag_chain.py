from src.utils.logger import logger


class RAGChain:

    def __init__(self, retriever, llm):

        self.retriever = retriever
        self.llm = llm

    def generate_answer(self, query: str):

        try:
            # Retrieve relevant chunks
            retrieved_docs = self.retriever.retrieve(query)

            # Handle empty retrieval
            if not retrieved_docs:

                logger.warning("No relevant documents retrieved")

                return {
                    "question": query,
                    "answer": "I don't know based on the document.",
                    "sources": []
                }

            # Build formatted context with citations
            context = "\n\n".join([
                f"""
Source: {doc.metadata.get("source", "Unknown")}
Page: {doc.metadata.get("page", "N/A")}

Content:
{doc.page_content}
"""
                for doc in retrieved_docs
            ])

            # Production-style prompt
             # Prompt template
            prompt = f"""
You are a factual and detailed AI assistant.

Answer the question using ONLY the provided context.

Rules:
- Do not use outside knowledge.
- Give detailed and well-structured explanations.
- Explain technical concepts clearly.
- Include important definitions, examples, and formulas if available in the context.
- Minimum answer length: 5 sentences.
- If the answer is not found in the context, say:
"I don't know based on the document."

Context:
---------------------
{context}
---------------------

Question:
{query}

Detailed Answer:
"""

            # Generate response
            response = self.llm.invoke(prompt)

            # Handle different response formats
            answer = (
                response.content
                if hasattr(response, "content")
                else str(response)
            )

            logger.info("Generated RAG response successfully")

            # Extract clean source metadata
            sources = []

            for doc in retrieved_docs:

                source_info = {
                    "source": doc.metadata.get("source", "Unknown"),
                    "page": doc.metadata.get("page", "N/A")
                }

                # Avoid duplicate sources
                if source_info not in sources:
                    sources.append(source_info)

            return {
                "question": query,
                "answer": answer,
                "sources": sources
            }

        except Exception as e:

            logger.error(f"RAG chain failed: {e}")

            raise