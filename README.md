# Cantonese Word and Character Frequencies

Frequency tables for Cantonese sourced from the LIHKG forum.

Corpus contains 50,611,075 sentences sourced from https://huggingface.co/datasets/AlienKevin/LIHKG. The sentences are segmented into words using pycantonese's tokenizer.

## Top 10 words
Full table see `word_freq.tsv`. Contains words of different lengths, including single characters.

| word | count    |
|------|----------|
| 都   | 7624851  |
| 係   | 6778612  |
| 我   | 6471541  |
| 唔   | 6210054  |
| 你   | 5818331  |
| 佢   | 4352672  |
| 好   | 4001553  |
| 咁   | 3305829  |
| 到   | 3126931  |
| 有   | 3008875  |

## words.hk list
See `word_freq.tsv` for a frequency table for all most words in the words.hk dictionary. 3605 words are missing in the corpus. You can see a full list of words in the dictionary in wordshk_words.json. Note that some words have multiple variant forms and they are treated as different words for counting purposes.
