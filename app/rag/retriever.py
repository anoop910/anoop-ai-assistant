import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document

from app.rag.embedding_model import Model


class Retriever:

    def __init__(self):

        self.index = faiss.read_index("vector.index")

        with open("documents.pkl", "rb") as f:
            self.documents: list[Document] = pickle.load(f)

    def search(self, query: str, k: int = 5):
        

        query_embedding = Model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        query_embedding = query_embedding.reshape(1, -1)

        scores, indices = self.index.search(query_embedding, k)

        return scores, indices