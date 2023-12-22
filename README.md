# Cantonese Word and Character Frequencies

Frequency tables for Cantonese sourced from popular online forums, TED talk transcription, and Linguistics corpus.

The tables are sorted in descending order first by `cantonese_count`s and uses the `mandarin_count`s as tie-breakers. Mandarin counts are derived from Mandarin sentences in the LIHKG forum as classified by [canto-filter](https://github.com/CanCLID/cantonese-classifier).

The size of the corpora used in this project is very small so the frequencies can only be taken as a very rough estimate. We also only include words from the words.hk dictionary so some words/characters might be excluded.

## Top 10 words
Full table see `word_freq.tsv`

| word | cantonese_count | mandarin_count |
|------|-----------------|----------------|
| 嘅   | 45136           | 0              |
| 係   | 32679           | 9              |
| 我   | 27629           | 14229          |
| 都   | 26625           | 14060          |
| 佢   | 23029           | 0              |
| 唔   | 19775           | 9              |
| 你   | 18775           | 10687          |
| 咗   | 16215           | 0              |
| 有   | 15868           | 12558          |
| 咁   | 14820           | 0              |

## Top 10 characters
Full table see `char_freq.tsv`

| char | cantonese_count | mandarin_count |
|------|-----------------|----------------|
| 係   | 62383           | 296            |
| 嘅   | 46226           | 0              |
| 唔   | 41472           | 9              |
| 我   | 35549           | 15292          |
| 好   | 31748           | 9393           |
| 有   | 31076           | 20352          |
| 個   | 29186           | 12531          |
| 佢   | 28650           | 0              |
| 都   | 28355           | 14147          |
| 一   | 28235           | 21427          |

## Compressed tables
Compressed tables sort all items by their `cantonese_count`s with `mandarin_count`s as tie-breakers. Next, items with `cantonese_count` or `mandarin_count` greater than or equal to 5 are kept. This threshold is chosen arbitrarily to cut off the long tail of infrequent items. Last, we discard the `mandarin_count`s.

# Corpus Used

1. [LIHKG Cantonese-Mandarin Corpus](https://huggingface.co/AlienKevin/LIHKG-Cantonese-Mandarin-Corpus)
2. [C4 Cantonese filtered](https://huggingface.co/datasets/indiejoseph/c4-cantonese-filtered)
3. [TED talk Cantonese transcriptions](https://huggingface.co/datasets/indiejoseph/ted-transcriptions-cantonese)
4. [HKCanCor](https://pycantonese.org/data.html#built-in-data)
