import json
from collections import defaultdict
from tqdm.contrib.concurrent import thread_map

all_words = set(json.load(open("wordshk_words.json", "r")))

print("Total words: {}".format(len(all_words)))

freq = defaultdict(int)

with open("freq.tsv", "r") as input:
    for line in input.readlines():
        word, count = line.strip().split("\t")
        if word in all_words:
            all_words.remove(word)
            freq[word] = int(count)

# Print missing words
print(f"Missing words: {len(all_words)}")

with open("words.txt", "r") as f:
    lines = f.readlines()
    def process_line(line_index):
        sent = lines[line_index].strip().replace(" ", "")
        for word in all_words:
            if word in sent:
                freq[word] += 1
    thread_map(process_line, range(len(lines)))

for word in all_words:
    if word in freq:
        all_words.remove(word)

# Print missing words
print(f"Missing words: {len(all_words)}")

with open("wordhk_freq.txt", "w+") as output:
    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        output.write("{}\t{}\n".format(word, count))
