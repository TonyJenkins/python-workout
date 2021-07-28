#!/usr/bin/env python3

"""
    Exercise 16: How Many Different Numbers

    Finds how many unqie values there are in a list of integers.
    Illustrate one use of sets. Could be done procedurally, which might
    make it more general.
"""


def how_many_different_numbers(numbers):
    return len(set(numbers))


if __name__ == '__main__':

    test_data = (
        [1, 2, 3],
        [1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 2],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        [],
    )

    for n in test_data:
        print(f'{n} -> {how_many_different_numbers(n)} unique number(s)')
