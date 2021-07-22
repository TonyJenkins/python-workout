#!/usr/bin/env python3

"""
    Additional: Absolute Value Sort (Exercise 11)

    Sort a sequence of positive and negative numbers based on absolute value.
"""


def abs_sort(numbers):
    return sorted(numbers, key=abs)


if __name__ == '__main__':

    values = (1, 2, 3, -1, -5, 6, 0, -2)

    print (abs_sort(values))

