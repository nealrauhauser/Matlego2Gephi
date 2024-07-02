#!/usr/bin/env python
import nltk
from collections import Counter
import sys

# Ensure you have the punkt tokenizer (only needed once)
nltk.download('punkt')

def character_count(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize the characters
    tokens = list(text)
    
    # Count the frequency of each character
    character_frequency = Counter(tokens)
    
    return character_frequency

# Example usage
char_count = character_count(sys.argv[1])

# Print character counts
for char, count in char_count.items():
    print(f"'{char}': {count}")

