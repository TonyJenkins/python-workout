#!/usr/bin/env python3

"""
    Exercise 45: Zoo

    A Zoo is a collection of cages, that contain animals.
"""


class Zoo:

    def __init__(self, name='Python Zoo'):
        self.name = name
        self.cages = []

    def add_cages(self, *cages):
        for each_cage in cages:
            self.cages.append(each_cage)

    def animals_by_colour(self, colour):
        return [
            animal
            for cage in self.cages
            for animal in cage.animals
            if animal.colour == colour
        ]

    def animals_by_legs(self, legs):
        return [
            animal
            for cage in self.cages
            for animal in cage.animals
            if animal.number_of_legs == legs
        ]

    def number_of_legs(self):
        legs = 0
        for cage in self.cages:
            for animal in cage.animals:
                legs += animal.number_of_legs

        return legs

    def __str__(self):
        output = self.name + '\n'

        if not self.cages:
            output += 'No animals in the Zoo'
        else:
            output += '\n'.join([str(each_cage) for each_cage in self.cages])

        return output
