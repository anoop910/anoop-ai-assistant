from pathlib import Path
from langchain_core.documents import Document

class MarkDownLoader:
    def __init__(self, knowlege_path: str) -> None:
        self.knowlege_path = Path(knowlege_path)
        
    def load(self) -> list[Document]:
        documents: list[Document] = []
        for file in self.knowlege_path.rglob("*.md"):
            content = file.read_text(encoding="utf-8")
            
            documents.append(Document(page_content=content, metadata={
                "source": str(file),
                "filename": file.name
            }))
        return documents