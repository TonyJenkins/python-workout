#!/usr/bin/env python3

"""
    Exercise 32: Flip a Dict

    "Flip" a dictionary by swapping keys and values.
"""


def flip(dictionary):
    return {v: k
            for k, v in dictionary.items()
            }


if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}

    print(f'{d} -> {flip(d)}')
