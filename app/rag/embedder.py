
from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document

class Embedder:
    def __init__(self) -> None:
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")
        
    def embed(self, documents: list[Document]):
        texts = [doc.page_content for doc in documents]
        embeddings = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        print(embeddings.shape)
        return embeddings