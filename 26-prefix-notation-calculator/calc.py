#!/usr/bin/env python3

"""
    Exercise 26: Prefix Notation Calculator

    Parse a string and evaluate the prefix expression therein.
        Illustrates a look-up table of functions in a dictionary.
"""

from operator import add, sub, mul, truediv, mod, pow


def calc(expression):
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '%': mod,
        '**': pow,
    }

    op, num1_str, num2_str = expression.split()

    return ops[op](int(num1_str), int(num2_str))


if __name__ == '__main__':

    expressions = [
        '* 2 3',
        '+ 10 4',
        '** 2 3',
        '/ 6 3',
        '% 7 3',
    ]

    for e in expressions:
        print(f'{e:8} -> {calc(e)}')
