#!/usr/bin/env python3

"""
    Exercise 38: Ice Cream Scoop

    Tester for the Scoop class.
"""

from scoop import Scoop


def create_scoops():

    s1 = Scoop('Chocolate')
    s2 = Scoop('Vanilla')
    s3 = Scoop('Persimmon')

    scoops = [s1, s2, s3]

    for scoop in scoops:
        print(scoop)


if __name__ == '__main__':
    create_scoops()

