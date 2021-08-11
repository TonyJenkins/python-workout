#!/usr/bin/env python3

"""
    Exercise 44: Cages

    Animals are now housed in cages.
"""

from animals import Parrot, Sheep, Snake, Wolf
from cage import Cage

if __name__ == '__main__':
    c = Cage()
    print(c)
    print()

    c2 = Cage()
    a_wolf = Wolf('grey')
    a_sheep = Sheep('black')
    a_snake = Snake('green')
    a_parrot = Parrot('red')

    c2.add_animals(a_wolf)
    print(c2)
    print()

    c2.add_animals(a_parrot, a_sheep, a_snake)
    print(c2)
    print()
