import json

min_count = 5

compressed_freq = {}

with open("word_freq.json", "r") as f:
    word_freq = json.loads(f.read())
    for word, [can_freq, man_freq] in word_freq.items():
        if can_freq >= min_count or man_freq >= min_count:
            compressed_freq[word] = [can_freq, man_freq]

with open("compressed_word_freq.json", "w") as f:
    f.write(json.dumps(compressed_freq, ensure_ascii=False))

with open("char_freq.json", "r") as f:
    char_freq = json.loads(f.read())
    compressed_char_freq = {char: freq for char, freq in char_freq.items() if freq >= min_count}

with open("compressed_char_freq.json", "w") as f:
    f.write(json.dumps(compressed_char_freq, ensure_ascii=False))
