# coding=utf-8
import yaml
import pathlib
import openai
from utils import get_config
from utils.openai_wrapper import ChatGPT

base_path = pathlib.Path.cwd().parent
config_file = base_path / 'config' / 'config.yaml'

with open(config_file, 'r') as inf:
    config = yaml.safe_load(inf)
config = get_config.run(config_file)

def main():
    text = """
    私の名前を知っていますか？
    """
    chatgpt = ChatGPT(config.openai_api_key, config.openai_model)
    print(chatgpt.run_chat(text))

if __name__ == '__main__':
    main()
