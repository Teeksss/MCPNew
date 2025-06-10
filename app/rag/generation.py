"""Simple generation utilities built on retrieval results."""

from typing import List


def generate_answer(contexts: List[str], query: str) -> str:
    """Generate an answer by concatenating retrieved contexts."""
    if not contexts:
        return "No relevant information found."
    return " ".join(contexts)
