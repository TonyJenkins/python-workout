#!/usr/bin/env python3

"""
    Exercise 28: Join Numbers

    Join together a range of numbers, comma-separated.
"""


def join_numbers(length):

    return ','.join(
                    [str(i)
                        for i in range(length)]
                    )


if __name__ == '__main__':

    print(join_numbers(10))
