#!/usr/bin/env python3

"""
    Exercise 31: Pig Latin Translation of a File

    Obfuscate a file using the simple "Pig Latin" rules.
"""


def pig_latin(word):

    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'way'


def pig_latin_file(filename):

    with open(filename) as in_file:
        return ' '.join(
            [
                pig_latin(word)
                for line in in_file
                for word in line.split()
            ])


if __name__ == '__main__':
    print (pig_latin_file('rev_eli.txt'))

