#!/usr/bin/env python3

"""
    Exercise 21: Longest Word per File

    Find the longest word in each text file in the current folder.
"""

from os import listdir


def find_longest_word(filename):
    longest = ''

    with open(filename, 'r', encoding='UTF8') as f:
        for line in f:
            for word in line.split():
                if len(word) > len(longest):
                    longest = word

    return longest


def find_all_longest_words():

    long_words = {}

    for filename in listdir('.'):
        if filename.endswith('.txt'):
            long_words[filename] = find_longest_word(filename)

    return long_words


if __name__ == '__main__':
    print(find_longest_word('jean_craig_graduate_nurse.txt'))

    print()

    for filename, word in find_all_longest_words().items():
        print(f'{filename:30} : {word}')
