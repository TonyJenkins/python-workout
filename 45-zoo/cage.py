#!/usr/bin/env python3

"""
    Exercise 44: Cages

    Animals are now housed in cages.
"""


class Cage:

    cage_counter = 0

    def __init__(self):
        Cage.cage_counter += 1
        self.id = Cage.cage_counter
        self.animals = []

    def add_animals(self, *new_animals):
        for animal in new_animals:
            self.animals.append(animal)

    def __str__(self):

        cage_id = f'Cage {self.id}\n'

        if self.animals:
            return cage_id + '\n'.join([str(animal) for animal in self.animals])
        else:
            return cage_id + 'Empty cage'
