use aho_corasick::{AhoCorasickBuilder, MatchKind};
use dashmap::DashMap;
use kdam::{rayon::prelude::*, TqdmParallelIterator};
use serde_json;
use std::collections::BTreeSet;
use std::fs::File;
use std::io::{self, BufRead, BufReader, Write};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Load the JSON file
    let file = File::open("wordshk_words.json")?;
    let reader = BufReader::new(file);
    let all_words: BTreeSet<String> = serde_json::from_reader(reader)?;

    println!("Total words: {}", all_words.len());

    // Initialize frequency map
    let freq = DashMap::new();

    // Read frequency data
    let freq_file = File::open("freq.tsv")?;
    let reader = BufReader::new(freq_file);
    for line in reader.lines() {
        let line = line?;
        let mut parts = line.split('\t');
        let word = parts.next().unwrap().to_string();
        let count = parts.next().unwrap().parse::<i32>()?;

        if all_words.contains(&word) {
            *freq.entry(word.clone()).or_insert(0) += count;
        }
    }

    // Remaining words
    let mut remaining_words = all_words
        .difference(&freq.iter().map(|entry| entry.key().clone()).collect())
        .cloned()
        .collect::<BTreeSet<String>>();
    println!("Missing words: {}", remaining_words.len());

    let ac = AhoCorasickBuilder::new()
        .match_kind(MatchKind::LeftmostLongest)
        .build(remaining_words.iter().cloned())
        .unwrap();

    // Process each line in parallel
    let lines: Vec<String> = BufReader::new(File::open("words.txt")?)
        .lines()
        .collect::<Result<Vec<_>, io::Error>>()?;
    lines.par_iter().tqdm().for_each(|line| {
        let sent = line.replace(" ", "");
        for mat in ac.find_iter(&sent) {
            *freq
                .entry(
                    remaining_words
                        .iter()
                        .nth(mat.pattern().as_usize())
                        .unwrap()
                        .clone(),
                )
                .or_insert(0) += 1;
        }
    });

    // Update remaining words
    remaining_words = remaining_words
        .difference(&freq.iter().map(|entry| entry.key().clone()).collect())
        .cloned()
        .collect::<BTreeSet<String>>();
    println!("Missing words: {}", remaining_words.len());

    // Write missing words to file
    let mut output = File::create("wordshk_missing.txt")?;
    for word in remaining_words {
        writeln!(output, "{}", word)?;
    }

    // Write to file
    let mut output = File::create("wordhk_freq.tsv")?;
    let mut freq_vec: Vec<_> = freq.into_iter().collect();
    freq_vec.sort_by(|a, b| b.1.cmp(&a.1));
    for (word, count) in freq_vec {
        writeln!(output, "{}\t{}", word, count)?;
    }

    Ok(())
}
