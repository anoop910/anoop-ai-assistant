import os

from groq import Groq
from dotenv import load_dotenv
from groq import RateLimitError

load_dotenv()


class GroqLlm:

    def __init__(self) -> None:

        my_api_key = os.getenv("GROQ_API_KEY")

        self.client = Groq(api_key=my_api_key)

        self.model = "llama-3.3-70b-versatile"

    def llmquery(self, systey_query: str, user_query: str):

        system_message = (
            {
                "role": "system",
                "content": systey_query,
            },
        )

        user_message = {"role": "user", "content": user_query}

        message = [system_message, user_message]

        try:

            response = self.client.chat.completions.create(
                model=self.model, messages=message
            )

            content = response.choices[0].message.content

            print(content)

            return content

        except RateLimitError as error:

            print("Groq rate limit reached!")

            raise error

    # ==========================================
    # STREAMING
    # ==========================================

    def llmquery_stream(self, systey_query: str, user_query: str):

        system_message = {
            "role": "system",
            "content": systey_query,
        }

        user_message = {"role": "user", "content": user_query}

        message = [system_message, user_message]

        try:

            response = self.client.chat.completions.create(
                model=self.model, messages=message, stream=True
            )

            for chunk in response:

                if not chunk.choices:
                    continue

                delta = chunk.choices[0].delta

                if delta.content:

                    yield delta.content

        except RateLimitError as error:

            print("Groq rate limit reached!")

            raise error
