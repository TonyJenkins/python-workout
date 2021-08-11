#!/usr/bin/env python3

"""
    Exercise 39: Ice Cream Bowl

    Using the Scoop class to make a complex ice cream dish (by composition).
"""


class Bowl:

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for each_scoop in new_scoops:
            self.scoops.append(each_scoop)

    def __str__(self):
        return ', '.join([str(scoop) for scoop in self.scoops])
