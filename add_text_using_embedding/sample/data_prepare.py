# coding=utf-8
import pandas as pd
import pathlib

base_path = pathlib.Path.cwd().parent.parent

def main():
    sample_file = base_path / 'add_text_using_embedding' / 'data' / 'sample_all.csv'
    end_file = base_path / 'add_text_using_embedding' / 'data' / 'sample.csv'
    df = pd.read_csv(sample_file, sep='\t')
    df = df.drop('abstract', axis=1)

    df['text'] = '--会社名:' + df["name"] + ' --勤務地:' + df["pref"] + ' --給与:' + df["salary"]  \
                  + ' --求人URL:' + df["url"] + ' --仕事の内容:' + df["detail"]
    df['text'].to_csv(end_file, index=False)


if __name__ == '__main__':
    main()
