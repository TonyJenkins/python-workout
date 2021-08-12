#!/usr/bin/env python3

"""
    Exercise 48: All lines, all files

    Generator to provide an iterator over all the files in a folder.
"""

from os import listdir
from os.path import join as path_join, isfile


def all_lines_all_files(path_to_folder):
    for filename in listdir(path_to_folder):
        full_filename = path_join(path_to_folder, filename)
        if isfile(full_filename):
            for each_line in open(full_filename):
                yield each_line[:-1]


if __name__ == '__main__':

    for line in all_lines_all_files('../45-zoo'):
        print(line)
