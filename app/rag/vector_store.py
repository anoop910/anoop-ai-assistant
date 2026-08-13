
import faiss
import pickle
from langchain_core.documents import Document
import numpy as np


class VectorStore:
    def __init__(self) -> None:
        self.index = None
        
    def build(self, embeddings: np.ndarray, documents: list[Document]):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)
        faiss.write_index(self.index, "vector.index")
        
        with open("documents.pkl", "wb") as f:
            pickle.dump(documents, f)