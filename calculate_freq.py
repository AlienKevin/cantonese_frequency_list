from collections import defaultdict
from tqdm import tqdm

freq = defaultdict(int)

with open("words.txt", "r") as f:
    for line in tqdm(f.readlines()):
        words = line.strip().split(" ")
        for word in words:
            freq[word] += 1

with open("freq.tsv", "w") as f:
    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        f.write("{}\t{}\n".format(word, count))
