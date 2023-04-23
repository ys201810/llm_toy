# coding=utf-8
import requests


class DeepL():
    def __init__(self, api_key: str, url: str):
        self.api_key = api_key
        self.url = url

    def run_translate(self, text: str, from_lang: str, to_lang: str) -> str:
        params = {
            'auth_key': self.api_key,
            'text': text,
            'source_lang': from_lang,  # 翻訳対象の言語
            "target_lang": to_lang  # 翻訳後の言語
        }
        translate_request = requests.post(self.url, data=params)

        translate_result = translate_request.json()
        return translate_result['translations'][0]['text']
