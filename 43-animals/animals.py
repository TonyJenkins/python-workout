#!/usr/bin/env python3

"""
    Exercise 43: Animals

    The specific animal classes.
"""

from animal import Animal


class Wolf(Animal):

    def __init__(self, colour):
        super().__init__('wolf', colour, 4)


class Sheep(Animal):

    def __init__(self, colour):
        super().__init__('sheep', colour, 4)


class Snake(Animal):

    def __init__(self, colour):
        super().__init__('snake', colour, 0)


class Parrot(Animal):

    def __init__(self, colour):
        super().__init__('parrot', colour, 2)


if __name__ == '__main__':

    a_wolf = Wolf('grey')
    a_sheep = Sheep('black')
    a_snake = Snake('green')
    a_parrot = Parrot('red')

    print(a_wolf)
    print(a_sheep)
    print(a_snake)
    print(a_parrot)
