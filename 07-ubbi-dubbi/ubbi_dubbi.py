#!/usr/bin/env python3

"""
    Exercise 07: Ubbi Dubbi

    Convert a word into a "Ubbi Dubbi". Sort of.
"""


def ubbi_dubbi(word):

    ubbi_letters = []

    for letter in word:
        ubbi_letters.append('ub' + letter if letter in 'aeiou' else letter)

    return ''.join(ubbi_letters)


if __name__ == '__main__':

    for word in ('milk', 'octopus', 'soap', 'bop', 'banana'):
        print(f'"{word}" ubbi dubbis to "{ubbi_dubbi(word)}".')
