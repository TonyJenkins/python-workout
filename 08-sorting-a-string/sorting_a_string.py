#!/usr/bin/env python3

"""
    Exercise 08: Sorting a String

    Sort a string based on Unicode value of its characters.
    Illustrates some string handling, and immutability.
"""


def strsort (s):
    return ''.join(sorted(s))


if __name__ == '__main__':

    for test_string in ('abc', 'cba', 'cheese', '', 'fedcba'):
        print(f'{test_string:10} sorts to "{strsort(test_string)}".')
