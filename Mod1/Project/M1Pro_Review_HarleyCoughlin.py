# This program reads a file and then outputs words that have only letters.
# 01/14/2025
# CSC221 M1Pro-Review
# Harley Coughlin

import Functions

def main():
    input_file = './words.txt'
    output_file = './replaced.txt'
    contents = None

    try:
        contents = Functions.read_file(filename=input_file)
    except FileNotFoundError:
        print(f'File {input_file} not found')

    if contents is not None:
        print(f'Total words: {Functions.word_count(contents)}')
        longest_word = Functions.longest_word(contents)
        if longest_word is not None:
            print(f'Longest word: {longest_word}')
        Functions.write_file(filename=output_file, lines=contents)


if __name__ == '__main__':
    main()
