#!/usr/bin/env python3

"""
    Exercise 38: Ice Cream Scoop

    Simple class for scoops of frozen treats.
"""


class Scoop:

    def __init__(self, flavour):
        self.flavour = flavour

    def __str__(self):
        return f'A scoop of {self.flavour}'
