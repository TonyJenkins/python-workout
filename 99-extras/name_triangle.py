#!/usr/bin/env python3

"""
    Additional: Name Triangle (Exercise 04)

    Prints an entered name in a triangle sort of thing.
"""


def name_triangle(name):

    for length, c in enumerate(name, start=1):
        print(name[:length])


if __name__ == '__main__':

    name = input('Enter your name: ')
    print()
    print('Generating your "Name Triangle" ...')
    name_triangle(name)
