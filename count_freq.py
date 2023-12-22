import os
from collections import defaultdict
from pathlib import Path
import json
from tqdm import tqdm

all_words = json.loads(open("words.json", "r").read())

can_word_freq = defaultdict(int)
can_char_freq = defaultdict(int)
man_word_freq = defaultdict(int)

can_dir = Path("lihkg/can")
man_dir = Path("lihkg/man")

# Read all sentences in can-xx.txt under lihkg/can
for can_file in os.listdir(can_dir):
    with open(can_dir/can_file, "r") as f:
        for line in f.readlines():
            words = line.strip().split(" ")
            for word in words:
                can_word_freq[word] += 1
                for char in word:
                    can_char_freq[char] += 1

for man_file in tqdm(os.listdir(man_dir)):
    with open(man_dir/man_file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            for word in all_words:
                if word in line:
                    man_word_freq[word] += 1

# merge can_word_freq with man_word_freq
word_freq = {}
for word in all_words:
    word_freq[word] = (can_word_freq[word], man_word_freq[word])

with open("word_freq.json", "w") as f:
    f.write(json.dumps(word_freq, ensure_ascii=False))
with open("char_freq.json", "w") as f:
    f.write(json.dumps(can_char_freq, ensure_ascii=False))
