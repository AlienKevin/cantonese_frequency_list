import os
from collections import defaultdict
from pathlib import Path
import json
import pycantonese

all_words = json.loads(open("words.json", "r").read())

can_word_freq = defaultdict(int)
can_char_freq = defaultdict(int)
man_word_freq = defaultdict(int)

can_dir = Path("lihkg/can")
lihkg_dir = Path("lihkg")
c4_dir = Path("c4-cantonese-filtered")
ted_dir = Path("ted-transcriptions-cantonese")

def update_can_freqs(words):
    global can_word_freq, can_char_freq
    for word in words:
        can_word_freq[word] += 1
        for char in word:
            can_char_freq[char] += 1

if __name__ == "__main__":
    corpus = pycantonese.hkcancor()
    update_can_freqs(corpus.words())

    # Read all sentences in can-xx.txt under lihkg/can
    for can_file in os.listdir(can_dir):
        with open(can_dir/can_file, "r") as f:
            for line in f.readlines():
                words = line.strip().split(" ")
                update_can_freqs(words)

    with open(c4_dir/"words.json", "r") as f:
        for sent in json.loads(f.read()):
            update_can_freqs(sent)

    with open(ted_dir/"words.json", "r") as f:
        for sent in json.loads(f.read()):
            update_can_freqs(sent)

    with open(lihkg_dir/"man_words.json", "r") as f:
        for sent in json.loads(f.read()):
            for word in sent:
                man_word_freq[word] += 1

    # merge can_word_freq with man_word_freq
    word_freq = {}
    for word in all_words:
        word_freq[word] = (can_word_freq[word], man_word_freq[word])

    with open("word_freq.json", "w") as f:
        f.write(json.dumps(word_freq, ensure_ascii=False))
    with open("char_freq.json", "w") as f:
        f.write(json.dumps(can_char_freq, ensure_ascii=False))
