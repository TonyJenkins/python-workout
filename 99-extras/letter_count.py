#!/usr/bin/env python3

"""
    Additional: Letter Count (Exercise 20)

    Find the most common letters in a file.
"""


from string import ascii_lowercase as letters


def letter_count(filename):

    counts = {}

    with open(filename) as f:
        while 1:
            c = f.read(1).lower()
            if not c:
                break
            elif c in letters:
                counts.setdefault(c, 0)
                counts[c] += 1

    print(sorted(counts, key=counts.get, reverse=True)[:5])


if __name__ == '__main__':
    letter_count('rev_eli.txt')
