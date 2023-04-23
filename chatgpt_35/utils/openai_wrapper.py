# coding=utf-8
import openai


class ChatGPT():
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def run_chat(self, text: str) -> str:
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "user", "content": text},
            ]
        )
        return response["choices"][0]["message"]["content"]
