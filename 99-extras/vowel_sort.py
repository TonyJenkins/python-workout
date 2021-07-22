#!/usr/bin/env python3

"""
    Additional: Vowel Count Sort (Exercise 11)

    Sort a sequence of strings based on the number of vowels therein.
"""


def vowel_count(string):

    count = 0
    for s in string:
        count += 1 if s in 'aeiou' else 0

    return count


def vowel_sort(strings):
    return sorted(strings, key=vowel_count)


if __name__ == '__main__':

    words = ('cheese', 'spam', 'eggs', 'beans', 'sausage', 'toast', 'fritter')
    print(vowel_sort(words))
