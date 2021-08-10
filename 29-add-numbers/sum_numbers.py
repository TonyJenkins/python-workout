#!/usr/bin/env python3

"""
    Exercise 29: Add Numbers

    Sum a sequence of numbers in a string, ignoring non-integers.
"""


def sum_numbers(number_string):

    numbers = [
        int(number)
        for number in number_string.split()
        if number.isdigit()
    ]

    return sum(numbers)


if __name__ == '__main__':

    print (sum_numbers(input('Enter a list of numbers: ')))
