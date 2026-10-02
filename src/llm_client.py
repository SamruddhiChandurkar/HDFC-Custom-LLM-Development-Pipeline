import os
import requests
from dotenv import load_dotenv

load_dotenv()


class LLMClient:

    def __init__(self):

        self.api_key = os.getenv("GROQ_API_KEY")

        self.model = os.getenv(
            "GROQ_MODEL",
            "openai/gpt-oss-120b"
        )

        self.url = (
            "https://api.groq.com/openai/v1/chat/completions"
        )

    def is_available(self):

        return bool(self.api_key)

    def generate(
        self,
        system_prompt,
        user_prompt,
        temperature=0.2,
        max_tokens=500
    ):

        if not self.api_key:

            raise RuntimeError(
                "GROQ_API_KEY is not configured."
            )

        headers = {
            "Authorization": (
                f"Bearer {self.api_key}"
            ),
            "Content-Type": "application/json"
        }

        payload = {

            "model": self.model,

            "messages": [

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }

            ],

            "temperature": temperature,

            "max_tokens": max_tokens
        }

        response = requests.post(

            self.url,

            headers=headers,

            json=payload,

            timeout=60
        )

        if response.status_code != 200:

            raise RuntimeError(

                f"Groq API error "
                f"{response.status_code}: "
                f"{response.text}"
            )

        data = response.json()

        return (
            data["choices"][0]["message"]["content"]
            .strip()
        )