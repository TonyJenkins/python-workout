#!/usr/bin/env python3

"""
    Exercise 37: Menu

    Generic menu function.
"""


def menu(header, **kwargs):

    valid_options = ', '.join(kwargs.keys())

    while True:
        print(f'{header.capitalize()} Menu')
        print(f'Options are: {valid_options}')
        choice = input('Enter option: ')

        if choice in kwargs.keys():
            return kwargs[choice]()

        print('Not a valid choice.')


if __name__ == '__main__':

    def func_a():
        return "Hello from Function A"

    def func_b():
        return "Hello from Function B"

    return_value = menu('Testing', a=func_a, b=func_b)
    print(f'Returned message is "{return_value}".')
