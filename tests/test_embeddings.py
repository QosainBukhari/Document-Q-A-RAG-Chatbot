from src.embeddings.embedding_model import EmbeddingModel

model = EmbeddingModel().get_model()

embedding = model.embed_query("What is machine learning?")

print(f"Embedding dimension: {len(embedding)}")