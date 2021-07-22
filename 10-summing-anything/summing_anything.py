#!/usr/bin/env python3

"""
    Exercise 10: Summing Anything

    Extending the bespoke "sum" function to work with different types.
    Illustrates how functions can (should) be generic. Obviously what
        "sum" does is determined by what "+" does.
"""


def mysum(*elements):

    if not elements:
        raise ValueError("Empty sequence passed to sum function")

    the_sum = elements[0]

    for e in elements[1:]:
        the_sum += e

    return the_sum


if __name__ == '__main__':

    print(mysum('abc', 'def'))
    print(mysum([1, 2, 3], [4, 5, 6]))
    print(mysum(1, 2, 3))

    print(mysum('a'))
    print(mysum(100))

    try:
        print(mysum())
    except ValueError as e:
        print(str(e))
