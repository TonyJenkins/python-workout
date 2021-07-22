#!/usr/bin/env python3

"""
    Additional: List Sum Sort (Exercise 11)

    Sort a list of lists based on the sum of the numbers therein.
        Sort in descending order because, well, why not.
"""

if __name__ == '__main__':

    numbers = [
        [97, 4],
        [1, 2, 3],
        [4, 5, 6],
        [1, 7, 8, 9],
        [22, 45],
        [1, 1, 1],
    ]

    for n in sorted(numbers, key=sum, reverse=True):
        print(f'{sum(n):8} : {n}')
