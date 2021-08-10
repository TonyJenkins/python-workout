#!/usr/bin/env python3

"""
    Exercise 30: Flatten a List

    Convert a list of lists into a single list.
        Two implementations. One with list comprehension, one without.
"""


def flatten(list_of_lists):
    return [
        an_element
        for each_list in list_of_lists
        for an_element in each_list
    ]


def flattenn(list_of_lists):
    flat_list = []

    for each_list in list_of_lists:
        for each_element in each_list:
            flat_list.append(each_element)

    return flat_list


if __name__ == '__main__':
    print(flatten([[1, 2], [3, 4]]))
    print(flattenn([[1, 2], [3, 4]]))
