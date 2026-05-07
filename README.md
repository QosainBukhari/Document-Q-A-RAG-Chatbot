# Document Q&A RAG Chatbot

Production-ready Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions using local Llama3 via Ollama, ChromaDB vector search, FastAPI, and Streamlit.

---

<p align="center">
  <img src="./asset/image_UI.png" width="900"/>
</p>
# Features

* PDF upload and processing
* Semantic search using vector embeddings
* ChromaDB vector database
* Local Llama3 inference via Ollama
* Grounded question answering
* Source citations with page numbers
* FastAPI REST API backend
* Streamlit frontend
* Persistent vector database
* Production-style modular architecture
* Config-driven setup
* Logging and error handling
* Startup model loading
* OpenAI integration support
* Hybrid local + cloud LLM architecture

---

# Tech Stack

* Python
* FastAPI
* Streamlit
* LangChain
* Ollama
* Llama3
* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings
* OpenAI API (Optional)

---

# Project Architecture

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Retriever
 ↓
LLM (Llama3 / OpenAI)
 ↓
Grounded Answer + Citations
```

---

# Project Structure

```text
Document-Q&A-RAG-Chatbot/
│
├── app/
│   ├── core/
│   ├── routes/
│   ├── services/
│   ├── main.py
│   └── schemas.py
│
├── src/
│   ├── embeddings/
│   ├── ingestion/
│   ├── llm/
│   ├── retriever/
│   ├── utils/
│   └── vectordb/
│
├── configs/
├── data/
├── logs/
├── models/
├── tests/
│
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/QosainBukhari/Document-Q-A-RAG-Chatbot.git

cd Document-Q-A-RAG-Chatbot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

## Install Ollama

Download from:

[Ollama Official Website](https://ollama.com/download?utm_source=chatgpt.com)

---

## Pull Llama3 Model

```bash
ollama pull llama3
```

---

## Start Ollama Server

```bash
ollama serve
```

---

# Environment Variables

Create a `.env` file:

```env
# =========================
# LLM Configuration
# =========================

LLM_PROVIDER=ollama

OLLAMA_MODEL=llama3
OLLAMA_BASE_URL=http://localhost:11434

OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini

# =========================
# Vector Database
# =========================

CHROMA_DB_DIR=./models/chroma_db

# =========================
# Embedding Models
# =========================

EMBEDDING_PROVIDER=local

EMBEDDING_MODEL=all-MiniLM-L6-v2
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
```

---

# Recommended Configuration

## Local Setup (Free)

Uses:

* Ollama + Llama3
* HuggingFace Embeddings

Best for:

* Learning
* Offline usage
* Development

---

## OpenAI Setup (Better Quality)

Uses:

* GPT-4o / GPT-4.1
* OpenAI Embeddings

Benefits:

* Better answer quality
* Stronger reasoning
* Reduced hallucinations
* Better retrieval grounding
* More accurate citations
* Improved formatting

Recommended Models:

| Task       | Model                  |
| ---------- | ---------------------- |
| LLM        | gpt-4o-mini            |
| Embeddings | text-embedding-3-small |

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Run Frontend

```bash
streamlit run streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# API Endpoints

## Health Check

```http
GET /health
```

---

## Upload PDF

```http
POST /upload
```

---

## Chat

```http
POST /chat
```

### Request

```json
{
  "question": "What is clustering?"
}
```

---

### Response

```json
{
  "question": "What is clustering?",
  "answer": "Clustering is the unsupervised task of grouping similar instances together.",
  "sources": [
    {
      "source": "ml_book.pdf",
      "page": 120
    }
  ]
}
```

---

# Example Workflow

1. Upload PDF document
2. Extract text from PDF
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in ChromaDB
6. Ask questions
7. Retriever fetches relevant chunks
8. LLM generates grounded answer
9. Sources returned with citations

---

# Production Features

* Modular architecture
* Persistent vector database
* Config-driven setup
* Logging system
* Error handling
* Source-aware citations
* Startup model loading
* Local + OpenAI support
* Clean API architecture
* Scalable RAG pipeline

---

# Future Improvements

* Multi-PDF support
* Conversation memory
* Hybrid search (BM25 + Vector Search)
* Streaming responses
* Authentication & authorization
* Docker deployment
* CI/CD pipeline
* Redis caching
* Async processing
* Kubernetes deployment
* Re-ranking pipeline
* Multi-user support

---

# Better RAG Quality Tips

For best answer quality:

* Use OpenAI embeddings
* Use GPT-4o or GPT-4.1
* Use smaller chunk sizes
* Add overlap during chunking
* Use metadata-aware retrieval
* Add citation-aware prompts
* Use temperature = 0 for factual QA

Recommended settings:

```python
temperature = 0
chunk_size = 500
chunk_overlap = 100
top_k = 4
```

---

# Author

## Qosain Bukhari

GitHub:
[QosainBukhari GitHub Repository](https://github.com/QosainBukhari/Document-Q-A-RAG-Chatbot?utm_source=chatgpt.com)

LinkedIn:
[Syed Qosain Bukhari LinkedIn](https://www.linkedin.com/in/syedqosainbukhari?utm_source=chatgpt.com)
