import json
import pandas as pd
import pycantonese

if __name__ == "__main__":
    c4 = pd.read_parquet("train-00000-of-00001-03ffec5dd433dd7e.parquet", engine='pyarrow')
    all_words = []

    for _, row in c4.iterrows():
        for sent in row["text"].split("\n"):
            words = pycantonese.segment(sent.strip())
            all_words.append(words)

    with open("words.json", "w+") as f:
        f.write(json.dumps(all_words, ensure_ascii=False))
