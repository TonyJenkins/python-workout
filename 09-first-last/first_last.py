#!/usr/bin/env python3

"""
    Exercise 09: First Last

    Find the first and last elements of a sequence, and return them
    in a sequence of the same type.
    Illustrates that functions can handle different types.
    Also some very cunning slicing. Doing this without a slice would fail because
        the extracted values are the wrong ("member") type.
"""


def firstlast(seq):
    return seq[:1] + seq[-1:]


if __name__ == '__main__':

    for s in (['abcd', ['a', 'b', 'c', 'd'], (3, 2, 1)]):

        print(f'{str(s):10} -> {firstlast(s)}')
