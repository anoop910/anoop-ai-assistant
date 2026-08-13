from app.llm.groq_llm import GroqLlm

from app.momery.in_memory import InMemoryConversation

from app.prompt.prompt_builder import get_promat
from app.prompt.query_rewrite import (
    get_query_rewrite_system_prompt,
    get_query_rewrite_user_prompt,
)

from app.llm.nvd_llm import NvdLLM


class ChatService:

    def __init__(self) -> None:

        self.groq = GroqLlm()

        self.conversation_memory = InMemoryConversation()

        self.nvd = NvdLLM()

    def chat(self, query: str, user_id: str):

        user_id = user_id

        conversation_id = user_id
        print(user_id)

        # ==========================================
        # GET PREVIOUS CHAT
        # ==========================================

        lastchat = self.conversation_memory.get_recent_messages(
            user_id=user_id, conversation_id=conversation_id
        )

        user_history = "\n".join(
            message["content"] for message in lastchat if message["role"] == "user"
        )

        # ==========================================
        # QUERY REWRITE
        # ==========================================

        query_rewrite_sy_prompt = get_query_rewrite_system_prompt(isNeed=True)

        query_rewrite_user_promat = get_query_rewrite_user_prompt(
            conversation=user_history, current_question=query
        )

        rewrite_query = self.nvd.generate(
            system_query=query_rewrite_sy_prompt, user_query=query_rewrite_user_promat
        )

        

        # ==========================================
        # BUILD PROMPT
        # ==========================================

        prompt = get_promat(
            retrieve_query=rewrite_query, user_id=user_id, user_query=query
        )

      

        # ==========================================
        # SAVE USER MESSAGE
        # ==========================================

        self.conversation_memory.add_message(
            user_id=user_id, conversation_id=user_id, role="user", content=query
        )

        # ==========================================
        # STREAM GROQ RESPONSE
        # ==========================================

        complete_response = ""

        for token in self.groq.llmquery_stream(systey_query=prompt, user_query=query):

            complete_response += token

            yield token

        # ==========================================
        # SAVE COMPLETE ASSISTANT RESPONSE
        # ==========================================

        self.conversation_memory.add_message(
            conversation_id=user_id,
            user_id=user_id,
            role="assistant",
            content=complete_response,
        )
