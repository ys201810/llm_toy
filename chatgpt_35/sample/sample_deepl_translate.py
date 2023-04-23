# coding=utf-8
import requests
import pathlib
from utils import get_config
from utils.deepl_wrapper import DeepL

base_path = pathlib.Path.cwd().parent
config_file = base_path / 'config' / 'config.yaml'

config = get_config.run(config_file)


def main():
    text = "At A Corporation, I led a project to optimize user engagement by predicting actions based on their web activity history, resulting in increased support content relevance and overall user satisfaction. Additionally, I successfully developed advanced algorithms for item recommendation systems, utilizing the latest in technology including recbole and bert4rec. I personally built and tested the recommendation system, which proved to be highly effective in improving user satisfaction and engagement. With my expertise in data analysis and algorithm development, I am confident in my ability to drive meaningful change in any role related to these areas."
    deepl = DeepL(config.deepl_api_key, config.deepl_url)
    translate_result = deepl.run_translate(
        text=text,
        from_lang='EN',
        to_lang='JP'
    )

    print(translate_result)


if __name__ == '__main__':
    main()
