#!/usr/bin/env python3

"""
    Exercise 35B: Gematria (Part 2)

    Calculate "Gematria" values for words.
"""

from random import shuffle
from string import ascii_lowercase as letters

WORD_FILE = 'words.txt'


def generate_letter_values():
    return {
        letter: ord(letter) - ord('a') + 1
        for letter in letters
    }


def gematria_for(word):
    letter_values = generate_letter_values()

    total = 0
    for letter in word:
        total += letter_values.get(letter, 0)

    return total


def gematria_equal(word):
    word_score = gematria_for(word)

    return [
        word[:-1].lower()
        for word in open(WORD_FILE)
        if gematria_for(word.lower()) == word_score
    ]


if __name__ == '__main__':

    test_word = input('Enter a word: ').lower()
    print(f'"{test_word}" has a gematria score of {gematria_for(test_word)}.')

    other_words = gematria_equal(test_word)

    print(f'There are {len(other_words)} words with the same score.')

    shuffle(other_words)
    print('For example:')
    for i in range(5 if len(other_words) >= 5 else len(other_words)):
        print(f'\t{other_words[i]}')
