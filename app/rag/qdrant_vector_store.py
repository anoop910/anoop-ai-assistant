import os
from re import S
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from qdrant_client.models import Document, PointStruct
from qdrant_client import models




class QdrantUtils:
    
    def __init__(self) -> None:
        load_dotenv()
        self.COLLECTION_NAME = "ANOOP-KNOWLEDGE-BASE"
        self.client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY"),
            cloud_inference=True
            )
 
    
    def test_connection(self):
        collections = self.client.get_collections()

        print("Qdrant connected successfully!")
        print(collections)
        
    def create_collection(self, collection_name: str):
        if not self.client.collection_exists(collection_name):
            self.client.create_collection(collection_name= collection_name,
                                          vectors_config=VectorParams(size=384, distance=Distance.COSINE,))
            print("Collection Created !")
        else:
            print("collection already exitst !")
    
    
    
    def store_chunk(self, text:str, id:int):
        self.create_collection(collection_name=self.COLLECTION_NAME)
        self.client.upsert(
        collection_name=self.COLLECTION_NAME,
        points = [
            PointStruct(
            id=id,
            vector=Document(
            text=text,
            model="sentence-transformers/all-MiniLM-L6-v2"),
            payload={"text": text}
                ),
            ]
        )
        
    def retrieve_chunk(self, query: str):
        results = self.client.query_points(
            collection_name=self.COLLECTION_NAME,
            query=Document(
            text=query,
            model="sentence-transformers/all-MiniLM-L6-v2",
            ),
            limit=5
            )  
        return results.points  

