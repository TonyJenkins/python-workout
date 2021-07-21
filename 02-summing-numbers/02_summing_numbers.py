#!/usr/bin/env python3

"""
    Exercise 02: Summing Numbers

    A function to sum up some numbers, illustrating functions and the splat operator.
"""


def mysum(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total


if __name__ == '__main__':
    print(mysum(1, 2, 3))
    print(mysum(10, 9, 8, 7, 6, 5))
