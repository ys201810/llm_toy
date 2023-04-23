# coding=utf-8
import pathlib
import openai
import tiktoken
import pandas as pd
from utils import get_config
from openai.embeddings_utils import distances_from_embeddings

base_path = pathlib.Path.cwd().parent.parent
config_file = base_path / 'config' / 'config.yaml'

config = get_config.run(config_file)
openai.api_key = config.openai_api_key


def main():
    sample_file = base_path / 'add_text_using_embedding' / 'data' / 'sample_bk.csv'
    end_file = base_path / 'add_text_using_embedding' / 'data' / 'sample.csv'
    df = pd.read_csv(sample_file, sep='\t')
    df = df.drop('abstract', axis=1)

    df['text'] = '--会社名: ' + df['name'] + ' --仕事の内容: ' + df['detail']
    df['text'].to_csv(end_file, index=False)
    df = pd.read_csv(end_file, sep='\t')

    tokenizer = tiktoken.get_encoding("cl100k_base")
    df['n_tokens'] = df.text.apply(lambda x: len(tokenizer.encode(x)))

    df['embeddings'] = df.text.apply(
        lambda x: openai.Embedding.create(
            input=x,
            engine='text-embedding-ada-002'
        )['data'][0]['embedding']
    )

    embedding_file = base_path / 'add_text_using_embedding' / 'data' / 'embeddings.csv'
    df.to_csv(embedding_file, index=False)

    question = '仕事の内容として、AIラボのような部署を持っている会社に興味があります。日本でおすすめの会社名を教えてください。'
    q_embeddings = openai.Embedding.create(
        input=question,
        engine='text-embedding-ada-002'
    )['data'][0]['embedding']

    df['distances'] = distances_from_embeddings(q_embeddings, df['embeddings'].values, distance_metric='cosine')

    cur_len = 0
    max_len = 2000
    returns = []
    for i, row in df.sort_values('distances', ascending=True).iterrows():
        # Add the length of the text to the current length
        cur_len += row['n_tokens'] + 4
        # If the context is too long, break
        if cur_len > max_len:
            break
        # Else add it to the text that is being returned
        returns.append(row["text"])
    context = "\n\n###\n\n".join(returns)

    response = openai.Completion.create(
        prompt=f"文脈を厳密に引用して質問に答えてください。\n\n文脈: {context}\n\n---\n\n質問: {question}\n回答:",
        temperature=0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        model='text-davinci-003',
    )

    print(response["choices"][0]["text"])

if __name__ == '__main__':
    main()
