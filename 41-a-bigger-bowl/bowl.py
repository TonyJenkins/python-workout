#!/usr/bin/env python3

"""
    Exercise 40: Bowl Limits

    Using the Scoop class to make a complex ice cream dish (by composition).
        Bowl can now contain no more than three scoops.
"""


class Bowl:

    MAX_SCOOPS = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for each_scoop in new_scoops:
            if len(self.scoops) < self.MAX_SCOOPS:
                self.scoops.append(each_scoop)

    def __str__(self):
        return ', '.join([str(scoop) for scoop in self.scoops])
