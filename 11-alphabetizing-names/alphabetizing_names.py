#!/usr/bin/env python3

"""
    Exercise 11: Alphabetizing Names

    Sort a list of dictionaries by an item within the dictionary.
"""

from operator import itemgetter

PEOPLE = [
    {'first': 'Tom', 'last': 'Smith', 'email': 'tom@smith.com'},
    {'first': 'Harry', 'last': 'Jones', 'email': 'harry@jones.com'},
    {'first': 'Emma', 'last': 'Brown', 'email': 'emma@brown.com'},
    {'first': 'Sarah', 'last': 'Brown', 'email': 'sarah@brown.com'},
]


def alphabetize_names():

    for p in sorted(PEOPLE, key=itemgetter('last', 'first')):
        print(f"{p['first']} {p['last']} : {p['email']}")


if __name__ == '__main__':

    alphabetize_names()
