#!/usr/bin/env python3

"""
    Exercise 46: MyEnumerate

    Implementation of the built-in enumerate to illsutrate iterators.
"""


class MyEnumerate:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        next_value = (self.index, self.data[self.index])
        self.index += 1

        return next_value


if __name__ == '__main__':

    for index, character in MyEnumerate('spam'):
        print(f'[{index}] => {character}')

    for interesting_tuple in MyEnumerate('eggs'):
        print(interesting_tuple)
