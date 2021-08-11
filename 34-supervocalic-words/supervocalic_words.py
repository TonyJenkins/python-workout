#!/usr/bin/env python3

"""
    Exercise 34: (Almost) Supervocalic Words

    Find a set of words that contain every vowel.
        Illustrates use of < to find subsets.
"""

WORD_FILE = 'words.txt'


def vowely_words(filename):

    vowels = set('aeiou')

    return {
        word[:-1]
        for word in open(filename)
        if vowels < set(word.lower())
    }


if __name__ == '__main__':

    words = vowely_words(WORD_FILE)

    for vowely_word in words:
        print(vowely_word)
