# coding=utf-8
import yaml
from collections import namedtuple


def run(config_file: str) -> (str, str):
    """
    APIKEYを取得する。
    :param config_file(str): APIKEYが記載されているyamlファイルのパス
    :return: openai_api_key(str), deepl_api_key(str): OpenAIとDeepLのAPIKEY
    """
    Config = namedtuple('Config',[
        'openai_api_key',
        'openai_model',
        'deepl_api_key',
        'deepl_url'
    ])

    with open(config_file, 'r') as inf:
        config = yaml.safe_load(inf)
    openai_api_key = config['openai']['api_key']
    openai_model = config['openai']['model']
    deepl_api_key = config['deepl']['api_key']
    deepl_url = config['deepl']['url']
    config = Config(
        openai_api_key=openai_api_key,
        openai_model=openai_model,
        deepl_api_key=deepl_api_key,
        deepl_url=deepl_url
    )

    return config

if __name__ == '__main__':
    run()
