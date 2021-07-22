#!/usr/bin/env python3

"""
    Additional: Odd Even Sums (Exercise 09)

    Find the sums of the odd and even elements in a list or tuple.
    Illustrates that they can be treated identically.
"""


def odd_even_sums(seq):

    if len(seq) < 2:
        raise ValueError('Sequence is too short')

    return [sum(seq[::2]), sum(seq[1::2])]


if __name__ == '__main__':

    for s in ([10, 20], [1, 2, 3, 4, 5, 6], [10, 20, 30, 40, 50, 60]):
        print(f'{str(s):30} -> {odd_even_sums(s)}')
