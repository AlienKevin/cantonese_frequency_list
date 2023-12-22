import json

# Print the top 100 most frequent words
print("Top 100 most frequent words")
with open("word_freq.json", "r") as f:
    word_freq = json.loads(f.read())
    for word in sorted(word_freq, key=lambda x: word_freq[x][0], reverse=True)[:100]:
        print(word, word_freq[word])

# Print the top 100 most frequent characters
print("Top 100 most frequent characters")
with open("char_freq.json", "r") as f:
    char_freq = json.loads(f.read())
    for char in sorted(char_freq, key=lambda x: char_freq[x], reverse=True)[:100]:
        print(char, char_freq[char])
