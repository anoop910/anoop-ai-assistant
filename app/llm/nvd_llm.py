import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class NvdLLM:

    def __init__(self) -> None:
        self.client = OpenAI(
            base_url=os.getenv("NVD_BASE_URL"), api_key=os.getenv("NVD_API_KEY")
        )

    def generate(self, system_query: str, user_query: str):

        system_message = {
            "role": "system",
            "content": system_query,
        }

        user_message = {"role": "user", "content": user_query}
        message = [system_message, user_message]
        completion = self.client.chat.completions.create(
            model="meta/muse-glimmer-30b",
            messages=message,
            temperature=1,
            top_p=0.95,
            max_tokens=8192,
            stream=False,
        )
        
        return completion.choices[0].message.content
