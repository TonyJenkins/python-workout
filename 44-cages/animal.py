#!/usr/bin/env python3

"""
    Exercise 42: Animals

    The base animal class.
        As it happens, an abstract class, but let's not get into that.
"""


class Animal:

    def __init__(self, species, colour, number_of_legs):
        self.species = species
        self.colour = colour
        self.number_of_legs = number_of_legs

    def __str__(self):
        return f'{self.colour} {self.species}, {self.number_of_legs} legs'
