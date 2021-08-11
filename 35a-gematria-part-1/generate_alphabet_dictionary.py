#!/usr/bin/env python3

"""
    Exercise 35A: Gematria (Part 1)

    Generate a dictionary of letters and number equivalents.
"""

from string import ascii_lowercase as letters


def generate_dictionary():

    return {
        letter: ord(letter) - ord('a') + 1
        for letter in letters
    }


if __name__ == '__main__':

    print(generate_dictionary())
