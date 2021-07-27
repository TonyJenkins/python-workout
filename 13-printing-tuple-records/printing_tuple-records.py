#!/usr/bin/env python3

"""
    Exercise 13: Printing Tuple Records

    Sort aand neatly display a list of tuples.
"""


from operator import itemgetter


def format_sort_records(records):

    output = []

    for record in sorted(records, key=itemgetter(1)):
        output.append(f'{record[0]:10} {record[1]:10} {record[2]:5.2f}')

    return '\n'.join(output)


if __name__ == '__main__':
    PEOPLE = [
        ('Donald', 'Trump', 7.85),
        ('Vladimir', 'Putin', 3.626),
        ('Jinping', 'Xi', 10.603),
        ('Boris', 'Johnson', 0.5),
    ]

    print(format_sort_records(PEOPLE))
