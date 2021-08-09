#!/usr/bin/env python3

"""
    Additional: Vowel Count in a File (Exercise 18)

    Count the number of vowels in a file.
"""


def file_vowel_count(filename):

    counts = {
        'a' : 0,
        'e' : 0,
        'i' : 0,
        'o' : 0,
        'u' : 0,
    }

    with open(filename) as f:
        while 1:
            c = f.read(1)
            if not c:
                break
            elif c in counts.keys():
                counts[c] += 1

    return counts


if __name__ == '__main__':

    print(file_vowel_count('rev_eli.txt'))
