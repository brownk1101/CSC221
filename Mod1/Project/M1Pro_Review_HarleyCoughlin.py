# This program reads a file and then outputs words that have only letters.
# 01/14/2025
# CSC221 M1Pro-Review
# Harley Coughlin

def main():
    punctuation = '.,;:?!'
    new_lines: list[list[str]] = []
    with open(file='words.txt', mode='r', encoding='utf-8') as input:
        # Loop through the lines in the file
        for line in input:
            # Strip white space and split
            words = line.strip().split()
            cleaned_words = []
            # For each word in the line
            for word in words:
                # Rebuild the word without the punctuation
                cleaned_word = ''.join(char for char in word if char not in punctuation)
                # Check if the word has any non-alphabetic characters
                if cleaned_word.isalpha():
                    # If the word is all alphabetic add it to the cleaned_words list
                    cleaned_words.append(cleaned_word)

            new_lines.append(cleaned_words)

    with open(file='replaced.txt', mode='w', encoding='utf-8') as output:
        for line in new_lines:
            output.write(' '.join(line) + '\n')


if __name__ == '__main__':
    main()
