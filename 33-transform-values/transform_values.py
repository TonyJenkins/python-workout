#!/usr/bin/env python3

"""
    Exercise 33: Transform Values

    Apply a function to each value in a dictionary.
"""


def transform_values(fn, dictionary):

    return {
        k: fn(v)
        for k, v in dictionary.items()
    }


if __name__ == '__main__':

    d = {'a': 1, 'b': 2, 'c': 3}
    d = transform_values(lambda x: x + 1, d)

    print(d)
