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

# Plot the distribution of word frequencies
import matplotlib.pyplot as plt
import numpy as np

word_freq = np.array([word_freq[word][0] for word in word_freq])
plt.hist(word_freq, bins=100, range=(0, 50))
plt.title("Word frequency distribution at the lower end")
plt.xlabel("Word frequency")
plt.ylabel("Number of words")
plt.show()
