# pip install ckip-transformers
from ckip_transformers.nlp import CkipWordSegmenter
from pathlib import Path
import os
import json
import torch

ws_driver  = CkipWordSegmenter(model="bert-base", device=torch.device("mps"))
man_dir = Path("man")
words = []

for man_file in os.listdir(man_dir):
    with open(man_dir/man_file, "r") as f:
        words.extend(ws_driver([line.strip() for line in f.readlines()]))

with open("man_words.json", "w+") as f:
    f.write(json.dumps(words, ensure_ascii=False))
