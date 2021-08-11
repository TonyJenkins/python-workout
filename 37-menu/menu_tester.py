#!/usr/bin/env python3

"""
    Exercise 37: Menu

    Testing the generic menu function.
"""

from menu import menu


def choose_spam():
    return 'Spam'


def choose_eggs():
    return 'Eggs'


def choose_beans():
    return 'Beans'


if __name__ == '__main__':
    chosen_item = menu('Cafe', spam=choose_spam, eggs=choose_eggs, beans=choose_beans)

    print(f'Item chosen was "{chosen_item}".')
