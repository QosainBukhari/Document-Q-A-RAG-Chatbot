from fastapi import APIRouter, Request

from app.schemas import ChatRequest
from app.services.rag_service import RAGService


router = APIRouter()


@router.post("/chat")
async def chat(
    request: Request,
    chat_request: ChatRequest
):

    try:

        # Access globally loaded resources
        vectordb = request.app.state.vectordb

        llm = request.app.state.llm

        # Create service
        rag_service = RAGService(
            vectordb,
            llm
        )

        # Generate response
        response = rag_service.ask_question(
            chat_request.question
        )

        return response

    except Exception as e:

        return {
            "error": str(e)
        }