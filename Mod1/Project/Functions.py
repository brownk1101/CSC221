# This module contains the i/o functions for M1Pro

def clean_word(word: str) -> str | None:
    punctuation = '.,;:?!'
    # Rebuild the word without punctuation.
    cleaned_word = ''.join(char for char in word if char not in punctuation)
    # If all characters in the word are alphabetical, return the word.
    if cleaned_word.isalpha():
        return cleaned_word
    return None

def read_file(filename: str) -> list[list[str]]:
    new_lines: list[list[str]] = []
    with open(file=filename, mode='r', encoding='utf-8') as file:
        for line in file:
            cleaned_words = []
            words = line.strip().split()
            for word in words:
                cleaned_word = clean_word(word)
                if cleaned_word is not None:
                    cleaned_words.append(cleaned_word) 
            # Chance that no words will get returned.
            if len(cleaned_words) > 0:
                new_lines.append(cleaned_words)
    return new_lines

def write_file(filename:str, lines: list[list[str]]) -> None:
    with open(file=filename, mode='w', encoding='utf-8') as file:
        for line in lines:
            # Rebuild the string and end with a newline.
            file.write(' '.join(line) + '\n')

def word_count(lines: list[list[str]]) -> int:
    total_words = 0
    for line in lines:
        total_words += len(line)
    return total_words

def longest_word(lines: list[list[str]]) -> str | None:
    longest_length = 0
    longest_word = None
    for line in lines:
        for word in line:
            if len(word) > longest_length:
                longest_length = len(word)
                longest_word = word
    return longest_word
