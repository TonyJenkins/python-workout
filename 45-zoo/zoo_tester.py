#!/usr/bin/env python3

"""
    Exercise 45: Zoo

    A Zoo is a collection of cages, that contain animals.
"""

from animals import Parrot, Sheep, Snake, Wolf
from cage import Cage
from zoo import Zoo

if __name__ == '__main__':

    a_wolf = Wolf('grey')
    a_sheep = Sheep('white')
    a_snake = Snake('green')
    a_parrot = Parrot('red')

    another_wolf = Wolf('black')
    another_sheep = Sheep('black')
    another_snake = Snake('brown')
    another_parrot = Parrot('green')

    cage_1 = Cage()
    cage_2 = Cage()
    cage_3 = Cage()

    cage_1.add_animals(a_wolf, a_sheep)
    cage_2.add_animals(a_snake, another_snake, a_parrot, another_parrot)
    cage_3.add_animals(another_sheep, another_wolf)

    the_zoo = Zoo('Testing Zoo')
    the_zoo.add_cages(cage_1, cage_2, cage_3)

    print(the_zoo)

    print()
    print('Black Animals')
    for animal in the_zoo.animals_by_colour('black'):
        print(animal)

    print()
    print('Two-legged Animals')
    for animal in the_zoo.animals_by_legs(2):
        print(animal)

    print()
    print(f'Total number of legs is {the_zoo.number_of_legs()}.')
