from typing import List

from langchain_community.embeddings import OllamaEmbeddings


def get_embedding_model() -> OllamaEmbeddings:
    """
    Returns Embedding Gemma running locally via Ollama.

    Prerequisites (outside Python):
    - Install Ollama
    - Run:
        ollama pull embeddinggemma:300m-bf16
    """
    return OllamaEmbeddings(model="embeddinggemma:300m-bf16")


def embed_texts(texts: List[str]) -> List[List[float]]:
    """Convenience helper to embed a list of texts."""
    model = get_embedding_model()
    return model.embed_documents(texts)



