"""Simple text retrieval utilities."""

from pathlib import Path
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

_DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "sample_docs.txt"

class Retriever:
    def __init__(self, data_file: Path = _DATA_FILE):
        self.documents = [line.strip() for line in data_file.read_text().splitlines() if line.strip()]
        self.vectorizer = TfidfVectorizer()
        self.doc_vectors = self.vectorizer.fit_transform(self.documents)

    def query(self, text: str, top_k: int = 3) -> List[str]:
        """Retrieve top_k relevant documents for the given text."""
        query_vec = self.vectorizer.transform([text])
        scores = linear_kernel(query_vec, self.doc_vectors).flatten()
        ranked_indices = scores.argsort()[::-1][:top_k]
        return [self.documents[idx] for idx in ranked_indices]
