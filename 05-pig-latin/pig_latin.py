#!/usr/bin/env python3

"""
    Exercise 05: Pig Latin

    Obfuscate a word using some simple rules.
    Illustrates some basic string munging.
"""


def pig_latin(word):

    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'way'


if __name__ == '__main__':

    while True:

        s = input('Enter a word to be converted to Pig Latin: ')

        if not s:
            break
        else:
            print(f'"{s}" in Pig Latin is "{pig_latin(s)}".')
