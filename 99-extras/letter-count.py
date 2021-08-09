#!/usr/bin/env python3

"""
    Additional: Letter Count (Exercise 20)

    Find the most common letters in a file.
"""


def letter_count(filename):

    counts = {
        'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0,
        'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0,
        'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0,
        'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0,
        'q' : 0, 'r' : 0, 's' : 0, 't' : 0,
        'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0,
        'y' : 0, 'z' : 0,
    }

    with open(filename) as f:
        while 1:
            c = f.read(1)
            if not c:
                break
            elif c.lower() in counts.keys():
                counts[c.lower()] += 1

    print(sorted(counts, key=counts.get, reverse=True)[:5])


if __name__ == '__main__':
    letter_count('rev_eli.txt')
