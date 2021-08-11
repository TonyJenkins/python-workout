#!/usr/bin/env python3

"""
    Exercise 39: Ice Cream Bowl

    Class tester for Bowl class.
"""

from bowl import Bowl
from scoop import Scoop

if __name__ == '__main__':

    the_bowl = Bowl()

    the_bowl.add_scoops(
        Scoop('Chocolate'),
        Scoop('Vanilla'),
        Scoop('Strawberry'),
    )

    print(the_bowl)
