##LLM_TOY
### chatgpt-35
#### コード
sample: chatgpt-3.5-turboでの会話用とdeeplの翻訳用と組み合わせのシンプルなコード
demo: 上記のデモ
utils: 汎用クラス

#### 使い方
llm_toy/config/config.yamlを作成し、以下のようなファイルを格納。

```
openai:
  api_key: {your_oepnai_key}
  model: gpt-3.5-turbo
deepl:
  api_key: {your_deepl_key}
  url: https://api-free.deepl.com/v2/translate
```

格納後、以下のコマンドで動作。

```
poetry install
python sample/sample_gpt35_talk.py
streamlit run demo/demo_gpt35_talk.py
```