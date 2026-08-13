# import json
# from app.llm.groq_llm import GroqLlm

# from app.chat_history.json_file_operation import JsonOperation
# # from app.llm.query_rewrite import QueryRewriter

# from app.prompt.prompt_builder import get_promat
# from app.prompt.query_rewrite import get_query_rewrite_system_prompt, get_query_rewrite_user_prompt
# groq = GroqLlm()
# chat = JsonOperation()
# # query_rewriter = QueryRewriter()



# while True:
#     query = input("Ask About Anoop : \n\n")
#     if query == "exit":
#         break
#     else:
#         lastchat = chat.get_last_messages(6)
        
#         user_history = "\n".join(
#             message["content"]
#             for message in lastchat
#                 if message["role"] == "user"
#                                 )

#         print(user_history)
#         query_rewrite_sy_prompt = get_query_rewrite_system_prompt()
#         query_rewrite_user_promat = get_query_rewrite_user_prompt(conversation=user_history, current_question=query)
#         rewrite_respose = groq.llmquery(systey_query=query_rewrite_sy_prompt, user_query=query_rewrite_user_promat)
#         # rewrite_respose = query_rewriter.rewrite(system_prompt=query_rewrite_sy_prompt, user_prompt=  query_rewrite_user_promat)
#         print(f"is need : {rewrite_respose}")
#         if rewrite_respose == "true":
#             query_rewrite_sy_prompt = get_query_rewrite_system_prompt(isNeed= True)
#             query_rewrite_user_promat = get_query_rewrite_user_prompt(conversation=user_history, current_question=query)
#             query = groq.llmquery(systey_query=query_rewrite_sy_prompt, user_query=query_rewrite_user_promat)
#             # query = query_rewriter.rewrite(system_prompt=query_rewrite_sy_prompt, user_prompt= query_rewrite_user_promat)
#         if rewrite_respose == "false":
#             print(f"passed query : {query}")
#             prompt = get_promat(query=query)
#             print("\n\n")
#             user_query_add_chat = {
#                 "role": "user",
#                 "content": query,
#             }
#             chat.add_chat_conversation(user_query_add_chat)
#             response = groq.llmquery(systey_query=prompt, user_query=query) 
#             response_add_chat = {
#                 "role":"assistant", 
#                 "content": response,
#             }
#             chat.add_chat_conversation(response_add_chat)
            
#         if rewrite_respose == "true": 
#              print(f"passed query : {query}")
#              prompt = get_promat(query=query)
#              user_query_add_chat = {
#                              "role": "user",
#                              "content": query,
#                          }
#              chat.add_chat_conversation(user_query_add_chat)
#              print("\n\n")
#              response = groq.llmquery(systey_query=prompt, user_query=query) 
#              response_add_chat = {
#                              "role":"assistant", 
#                              "content": response,
#                          }
#              chat.add_chat_conversation(response_add_chat)
       




# from app.rag.splitter import MarkdownTextChunker
# from app.rag.qdrant_vector_store import QdrantUtils

# def print_search_results(points):
#     print("\n" + "=" * 80)
#     print("                 SEARCH RESULTS")
#     print("=" * 80)

#     for rank, point in enumerate(points, start=1):

#         payload = point.payload or {}

#         print("\n" + "-" * 80)
#         print(f"Rank  : {rank}")
#         print(f"Score : {point.score:.4f}")
#         print(f"ID    : {point.id}")

#         print("\nContent:")
#         print(payload.get("text", ""))

#     print("\n" + "=" * 80)
#     print(f"Total Results: {len(points)}")
#     print("=" * 80)
# # chunker = MarkdownTextChunker()
# qdrant = QdrantUtils()
# # chunks = chunker.chunk()
# # for i, chunk in enumerate(chunks):
# #     text = str(chunk)
# #     qdrant.store_chunk(id=i, text=text)
# #     print(f"upload chunk no {i}")


# results = qdrant.retrieve_chunk(query="who is anoop")
# print_search_results(results.points)

# while True:
#     query = input("entry your query: \n")
#     if query == exit:
#         break
#     else:
#         results = qdrant.retrieve_chunk(query=query)
#         print_search_results(results.points)

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router
import os

load_dotenv()
app = FastAPI(
    title="Anoop AI Assistant"
)

cors_origins_string = os.getenv(
    "CORS_ORIGINS",
    ""
)
cors_origins = [
    origin.strip()
    for origin in cors_origins_string.split(",")
    if origin.strip()
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


        
