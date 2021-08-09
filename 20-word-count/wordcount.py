#!/usr/bin/env python3

"""
    Exercise 20: Word Count

    Mimic the Un*x "wc" command to count lines, words, and characters.
"""


def wc(filename):

    lines = 0
    words = 0
    characters = 0

    distinct_words = set()

    with open(filename) as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)
            distinct_words.update(line.split())

    print(f'Characters:     {characters}.')
    print(f'Words:          {words}.')
    print(f'Distinct Words: {len(distinct_words)}.')
    print(f'Lines:          {lines}.')


if __name__ == '__main__':

    wc('wcfile.txt')
    print()
    wc('rev_eli.txt')
