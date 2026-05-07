import shutil
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, Request

from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.chunker import TextChunker
from src.vectordb.chroma_store import ChromaVectorStore


router = APIRouter()

UPLOAD_DIR = "data/raw"

Path(UPLOAD_DIR).mkdir(
    parents=True,
    exist_ok=True
)


@router.post("/upload")
async def upload_pdf(
    request: Request,
    file: UploadFile = File(...)
):

    try:

        # Validate extension
        if not file.filename.endswith(".pdf"):

            return {
                "error": "Only PDF files allowed"
            }

        # Save uploaded file
        file_path = f"{UPLOAD_DIR}/{file.filename}"

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        # Load PDF
        loader = PDFLoader(file_path)

        documents = loader.load_pdf()

        # Chunking
        chunker = TextChunker()

        chunks = chunker.create_chunks(
            documents
        )

        # Access globally loaded embedding model
        embedding_model = (
            request.app.state.embedding_model
        )

        # Create vector DB
        vectordb = ChromaVectorStore(
            embedding_model
        )

        vectordb.create_vector_store(chunks)

        return {
            "message": "PDF uploaded successfully",
            "filename": file.filename,
            "total_chunks": len(chunks)
        }

    except Exception as e:

        return {
            "error": str(e)
        }