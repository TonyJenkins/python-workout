#!/usr/bin/env python3

"""
    Exercise 27: Password Generator

    Generate random passwords from pools of characters.
        Actually generates functions that generate passwords.
"""

import random
from string import ascii_letters as letters
from string import punctuation as special_characters
from string import digits as digits


def create_password_generator(character_pool):

    def create_password(length):
        passwd = ''
        for i in range(length):
            passwd += random.choice(character_pool)

        return passwd

    return create_password


if __name__ == '__main__':

    generate_letter_password = create_password_generator(letters)
    generate_better_password = create_password_generator(letters + digits)
    generate_complex_password = create_password_generator(letters + digits + special_characters)

    print(generate_letter_password(10))
    print(generate_better_password(12))
    print(generate_complex_password(8))
    
