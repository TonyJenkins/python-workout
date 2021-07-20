#!/usr/bin/env python3

"""
    Exercise 01: Number Guessing Game

    A simple guessing game, showing basic input / output and use of a function from a built-in module.
"""

from random import randint


def guessing_game():
    secret = randint(0, 100)

    while True:
        guess = int(input('Enter your guess: '))

        if guess == secret:
            print(f'Well done. You guessed it right. The number was {secret}.')
            break
        elif guess > secret:
            print(f'Your guess of {guess} was too high.')
        elif guess < secret:
            print(f'Your guess of {guess} was too low.')


if __name__ == '__main__':
    guessing_game()
