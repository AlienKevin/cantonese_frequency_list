import json
import pandas as pd
import pycantonese

if __name__ == "__main__":
    c4 = pd.read_parquet("train-00000-of-00001-a09588dedc558888.parquet", engine='pyarrow')
    all_words = []

    for _, row in c4.iterrows():
        words = pycantonese.segment(row["text"])
        all_words.append(words)

    with open("words.json", "w+") as f:
        f.write(json.dumps(all_words, ensure_ascii=False))
