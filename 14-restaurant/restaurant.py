#!/usr/bin/env python3

"""
    Exercise 14: Restaurant

    Find the value of a restaurant order using a dictionary.
"""

MENU = {
    'tea': 7,
    'sandwich': 10,
    'apple': 3,
    'coffee': 6,
    'lemonade': 4,
    'chips': 6,
    'toastie': 11,
}


def restaurant():

    total = 0

    while True:
        item = input('Order: ').strip()

        if not item:
            break

        if item in MENU:
            total += MENU[item]
            print(f'{item} costs {MENU[item]}, total is {total}.')
        else:
            print(f'We are right out of {item} today, unfortunately.')

    return total


if __name__ == '__main__':
    print('Your total is', restaurant())
