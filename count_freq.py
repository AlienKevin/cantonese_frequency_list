import os
from collections import defaultdict
from pathlib import Path
import json
import pycantonese
import csv
import regex as re

cjk_pattern = re.compile(r"\p{Unified_Ideograph}")

all_words = json.loads(open("words.json", "r").read())
all_chars = { char for word in all_words for char in word if cjk_pattern.match(char) }

can_word_freq = defaultdict(int)
can_char_freq = defaultdict(int)
man_word_freq = defaultdict(int)
man_char_freq = defaultdict(int)

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

def dump_freq(item_name: str, freq: dict, f):
    fieldnames = [item_name, "cantonese_count", "mandarin_count"]
    writer = csv.DictWriter(f, delimiter='\t', fieldnames=fieldnames)
    writer.writeheader()
    for key, (can_freq, man_freq) in freq.items():
        writer.writerow({ item_name: key, "cantonese_count": can_freq, "mandarin_count": man_freq })

def sort_dict_by_value(d: dict):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

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
                for char in word:
                    man_char_freq[char] += 1

    # merge can_word_freq with man_word_freq
    word_freq = {}
    for word in all_words:
        word_freq[word] = (can_word_freq[word], man_word_freq[word])

    # merge can_char_freq with man_char_freq
    char_freq = {}
    for char in all_chars:
        char_freq[char] = (can_char_freq[char], man_char_freq[char])

    with open("word_freq.tsv", "w") as f:
        dump_freq("word", sort_dict_by_value(word_freq), f)
    with open("char_freq.tsv", "w") as f:
        dump_freq("char", sort_dict_by_value(char_freq), f)
