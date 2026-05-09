from src.embeddings.embedding_model import EmbeddingModel


def test_embeddings():

    model = EmbeddingModel().get_model()

    embedding = model.embed_query(
        "What is machine learning?"
    )

    assert embedding is not None

    assert len(embedding) > 0