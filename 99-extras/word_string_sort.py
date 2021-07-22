#!/usr/bin/env python3

"""
    Additional: Word String Sort (Exercise 08)

    Print a comma-separated list of the words in a string, sorted.
"""

if __name__ == '__main__':

    while True:

        words = input('Enter some words to sort: ')

        if not words:
            break

        print(','.join(sorted(words.split())))
