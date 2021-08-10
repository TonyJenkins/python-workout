#!/usr/bin/env python3

"""
    Exercise 24: Reverse Lines

    Reverse all the lines in a text file.
"""


from os.path import splitext


def reverse_lines(filename):

    outfile = f'{splitext(filename)[0]}_reversed{splitext(filename)[1]}'

    with open(filename) as original, open(outfile, 'w') as reversed_file:
        for line in original:
            reversed_file.write(line[:-1][::-1] + '\n')


if __name__ == '__main__':

    reverse_lines('rev_eli.txt')
