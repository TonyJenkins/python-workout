#!/usr/bin/env python3

"""
    Additional: Multiple Copies of a File (Exercise 25)

    Generate copies of a file based on function paramarters.
"""


from shutil import copyfile


def multi_copy(original, *copies):

    if not copies:
        raise ValueError('Missing file names for copies to be generated.')

    for copy in copies:
        copyfile(original, copy)


if __name__ == '__main__':

    multi_copy('rev_eli.txt', 'eli2.txt')
    multi_copy('rev_eli.txt', 'eli2.txt', 'eli3.txt')

    try:
        multi_copy('rev_eli.txt')
    except ValueError as e:
        print(e)
