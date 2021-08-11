#!/usr/bin/env python3

"""
    Exercise 36: Sales Tax

    Somewhat whimsical sales tax function, in a module.
"""

TAX_RATES = {
    'Chico': 0.5,
    'Groucho': 0.7,
    'Harpo': 0.5,
    'Zeppo': 0.4,
}


def hour_factor(hour):
    if hour not in range(24):
        raise ValueError('Invalid hour for purchase')

    return hour / 24


def calculate_tax(price, province, hour):

    return price + (price * TAX_RATES[province] * hour_factor(hour))


if __name__ == '__main__':

    print(calculate_tax(500, 'Harpo', 12))
