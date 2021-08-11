#!/usr/bin/env python3

"""
    Additional: Files and Sizes in the Current Folder (Exercise 32)

    Create a dictionary of the current folder's files and their sizes.
"""

from os import listdir
from os.path import getsize


def file_dict():

    return {file: getsize(file)
            for file in listdir()
            }


if __name__ == '__main__':

    print(file_dict())
