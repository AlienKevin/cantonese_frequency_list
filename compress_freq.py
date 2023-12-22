import csv

min_count = 5

# Compress the frequency data by removing words with low frequency
# Also keep only Cantonese frequency after sorting
def compress(item_name: str):
    compressed_freq = []

    # Read and filter item frequency
    with open(f"{item_name}_freq.tsv", mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)

        for row in reader:
            word, can_freq, man_freq = row
            can_freq, man_freq = int(can_freq), int(man_freq)
            if can_freq >= min_count or man_freq >= min_count:
                compressed_freq.append([word, can_freq])

    # Write filtered data to TSV
    with open(f"compressed_{item_name}_freq.tsv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(header[:2])
        writer.writerows(compressed_freq)

if __name__ == "__main__":
    compress("word")
    compress("char")
