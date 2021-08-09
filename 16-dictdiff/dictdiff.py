#!/usr/bin/env python3

"""
    Exercise 16: Dictdiff

    Gather and summarise rainfall data.
"""


def dictdiff(dict1, dict2):

    result = {}

    for key in dict1.keys() | dict2.keys():
        if dict1.get(key) != dict2.get(key):
            result[key] = [dict1.get(key), dict2.get(key)]

    return result

    
if __name__ == '__main__':

    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}

    print(dictdiff(d1, d1))
    print(dictdiff(d1, d2))

    d3 = {'a': 1, 'b': 2, 'd': 3}
    d4 = {'a': 1, 'b': 2, 'c': 4}

    print(dictdiff(d3, d4))
    d5 = {'a': 1, 'b': 2, 'd': 4}

    print(dictdiff(d1, d5))
