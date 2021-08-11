#!/usr/bin/env python3

"""
    Exercise 40: Ice Cream Bowl Limit

    Class tester for Bowl class.
"""

from big_bowl import BigBowl
from bowl import Bowl
from scoop import Scoop

if __name__ == '__main__':

    the_bowl = Bowl()
    the_big_bowl = BigBowl()

    the_bowl.add_scoops(
        Scoop('Chocolate'),
        Scoop('Vanilla'),
        Scoop('Mint Choc Chip'),
        Scoop('Rum and Raisin'),
        Scoop('Strawberry'),
    )

    the_big_bowl.add_scoops(
        Scoop('Chocolate'),
        Scoop('Vanilla'),
        Scoop('Mint Choc Chip'),
        Scoop('Rum and Raisin'),
        Scoop('Strawberry'),
    )

    print(f'Adding to a standard bowl: {the_bowl}')
    print(f'Adding to a bigger bowl:   {the_big_bowl}')
