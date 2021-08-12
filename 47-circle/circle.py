#!/usr/bin/env python3

"""
    Exercise 47: Circle

    An iterator that repeats elements from a sequence.
"""


class CircleIterator:

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration

        next_value = self.data[self.index % len(self.data)]
        self.index += 1

        return next_value


class Circle:
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CircleIterator(self.data, self.max_times)


if __name__ == '__main__':

    c = Circle('abcd', 7)

    for e in enumerate(c):
        print(e)
