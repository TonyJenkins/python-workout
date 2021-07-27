#!/usr/bin/env python3

"""
    Exercise 12: Word with Most Repeating Letters

    Find the word with the most repeated letters in a sequence.
"""

from collections import Counter


def most_common_letter(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    return max(words, key=most_common_letter)


if __name__ == '__main__':
    WORDS = [
        'spam',
        'eggs',
        'banana',
        'turnip',
        'cheese',
        'newt',
    ]

    print(most_repeating_word(WORDS))
