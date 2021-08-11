#!/usr/bin/env python3

"""
    Exercise 42: FlexibleDict

    A specialised version of a dictionary that allows ints and strs as
        interchangeable keys.
"""

class FlexibleDict(dict):

    def __getitem__(self, key):

        if key in self:
            pass
        elif str(key) in self:
            key = str(key)
        elif int(key) in self:
            key = int(key)

        return dict.__getitem__(self, key)


if __name__ == '__main__':

    flex = FlexibleDict()

    flex['a'] = 100
    print(flex['a'])

    flex[5] = 200
    print(flex[5])
    print(flex['5'])

    flex['1'] = 300
    print(flex[1])
