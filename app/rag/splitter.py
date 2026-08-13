


from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter

from app.rag.loader import MarkDownLoader
from app.rag.qdrant_vector_store import QdrantUtils
class MarkdownTextChunker:
    path = "D:\\Ai_Project\\anoop-ai-assistant\\app\\knowledge"
    test_path = "D:\\Ai_Project\\anoop-ai-assistant\\app\\test_knowledgebase"
    headers_to_split_on = [
    ("#", "Header 1"),
    # ("##", "Header 2"),
    # ("###", "Header 3"),
    ]

    def __init__(self) -> None:
        self.splitter = MarkdownHeaderTextSplitter(headers_to_split_on=self.headers_to_split_on)
        self.document_loader = MarkDownLoader(self.path)
        self.qdrant = QdrantUtils()
        
        
    def chunk(self) -> list:
        documents = self.document_loader.load()
        all_chunks: list[Document] = []
        
        for file in documents:
            chunks = self.splitter.split_text(file.page_content)
            all_chunks.extend(chunks)
        return all_chunks
         
               
               
              
              

        