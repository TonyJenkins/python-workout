#!/usr/bin/env python3

"""
    Exercise 18: Final Line

    Display the final (last) line of a file.
"""


def get_final_line(filename):

    f = open(filename)
    line = f.readlines()[-1][:-1]
    f.close()

    return line


if __name__ == '__main__':

    print(get_final_line('rev_eli.txt'))

