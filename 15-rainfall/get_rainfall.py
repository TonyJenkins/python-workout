#!/usr/bin/env python3

"""
    Exercise 15: Rainfall

    Gather and summarise rainfall data.
"""


def get_rainfall():

    rainfalls = {}
    while True:
        city = input('Enter City: ')

        if not city:
            break
        else:
            try:
                rain = int(input('Enter Rain: '))
                rainfalls[city] = rainfalls.get(city, 0) + rain
            except ValueError:
                print('Non-integer entered. Data ignored.')

    print()
    for city, rain in rainfalls.items():
        print(f'{city}: {rain}')


if __name__ == '__main__':
    get_rainfall()
