from fastapi import FastAPI

from app.core.startup import load_models

from app.routes.upload import router as upload_router
from app.routes.chat import router as chat_router


app = FastAPI(
    title="RAG Chatbot API"
)


@app.on_event("startup")
async def startup_event():

    load_models(app)


@app.get("/health")
async def health_check():

    return {
        "status": "ok"
    }


# Register routes
app.include_router(upload_router)

app.include_router(chat_router)