#!/usr/bin/env python3

"""
    Exercise 04: Hexadecimal Output

    Convert an entered hex number into decimal.
    Note: Unlike the book solution, this program handles hex (A-F) characters in the input.
"""


def hex_to_dec(hex_string):

    HEX_DIGITS = '0123456789ABCDEF'
    dec = 0

    for power, c in enumerate(reversed(hex_string)):
        if c not in HEX_DIGITS:
            raise ValueError('Non-hex digit passed as input to conversion')
        dec += HEX_DIGITS.find(c) * (16 ** power)

    return dec


if __name__ == '__main__':
    print(hex_to_dec('A'))
