#!/usr/bin/env python3

"""
    Exercise 36: Sales Tax

    Somewhat whimsical sales tax function: driver program.
"""

import freedonia


if __name__ == '__main__':

    print(f'{freedonia.calculate_tax(500, "Harpo", 0):.2f}')
    print(f'{freedonia.calculate_tax(400, "Groucho", 23):.2f}')
    print(f'{freedonia.calculate_tax(0, "Chico", 1):.2f}')
