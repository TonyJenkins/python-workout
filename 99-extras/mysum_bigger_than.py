#!/usr/bin/env python3

"""
    Additional: Summing Anything Bigger Than (Exercise 10)

    Variation on the "mysum" function that has an additional first
    parameter, and only sums elements greater than that.
    A handy example of using "None" to create a variable with no value.
"""


def mysum(*elements):

    if len(elements) <= 1:
        raise ValueError("Short sequence passed to sum function")

    min_value = elements[0]
    the_sum = None

    for e in elements[2:]:
        if e > min_value:
            if not the_sum:
                the_sum = e
            else:
                the_sum += e

    return the_sum


if __name__ == '__main__':

    print(mysum('bbb', 'abc', 'def'))
    print(mysum([1], [1, 2, 3], [4, 5, 6]))
    print(mysum(2, 1, 2, 3))

    try:
        print(mysum('a'))
        print(mysum(100))
        print(mysum())
    except ValueError as err:
        print(str(err))
