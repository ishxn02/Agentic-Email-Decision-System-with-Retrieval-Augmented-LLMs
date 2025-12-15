from typing import List, Dict

import numpy as np

from embeddings import get_embedding_model


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Compute cosine similarity between two embedding vectors."""
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def retrieve_similar_cases(
    query_summary: str, past_cases: List[Dict[str, str]], top_k: int = 2
) -> List[str]:
    """
    Use Embedding Gemma to find the most similar past email summaries.
    Returns the summaries of the top_k most similar cases.
    """
    embed_model = get_embedding_model()

    # Embed query and past cases
    query_emb = np.array(embed_model.embed_query(query_summary))
    case_summaries = [case["summary"] for case in past_cases]
    case_embs = np.array(embed_model.embed_documents(case_summaries))

    # Compute cosine similarity scores
    scores = [cosine_similarity(query_emb, emb) for emb in case_embs]

    # Rank and return top_k summaries
    ranked_indices = np.argsort(scores)[::-1][:top_k]
    return [case_summaries[i] for i in ranked_indices]


# Simple in-memory historical dataset to simulate a vector DB.
HISTORICAL_CASES: List[Dict[str, str]] = [
    {
        "summary": "Database outage in production causing login failures",
        "label": "critical_incident",
    },
    {
        "summary": "Customer asking about refund policy for last month’s invoice",
        "label": "billing_query",
    },
    {
        "summary": "Reminder: monthly performance review meeting next Tuesday",
        "label": "meeting",
    },
    {
        "summary": "Low-severity bug reported in staging environment",
        "label": "bug_report",
    },
]


