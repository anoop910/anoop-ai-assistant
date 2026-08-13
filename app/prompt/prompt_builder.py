

from qdrant_client.models import Payload

# from app.chat_history.json_file_operation import JsonOperation
from app.momery.in_memory import InMemoryConversation
from app.prompt.converstion_system_prompt import get_system_prompt
from app.rag.qdrant_vector_store import QdrantUtils

# from app.rag.retriever import Retriever

# retriever = Retriever()

qdrant = QdrantUtils()
convesation_memory = InMemoryConversation()



   
def get_promat(retrieve_query: str, user_id:str, user_query: str):
    list_chunk = retrieve_chunk(query=retrieve_query)
    prompt_build = prompt(context=list_chunk, user_id=user_id, user_query= user_query)
    return prompt_build
    
            
          



def retrieve_chunk(query: str):
    texts = list()
    results = qdrant.retrieve_chunk(query=query)
    for rank, point in enumerate(results, start=1):
        payload = point.payload or {}
        text = payload.get("text", "")
        texts.append(text)
    return texts
  

def prompt(user_query:str, context: list, user_id: str):
    
    last_messages = convesation_memory.get_recent_messages(user_id=user_id, conversation_id=user_id, limit=4)
    # print(last_messages)
    
    prompt = f"""
    {get_system_prompt()}

    PRIVOUS CONVERSATION:
    {last_messages}
   
    RETRIEVED CONTEXT:
    {context}
    CURRENT USER QUESTION
    {user_query}
    
    """
    
    return prompt
