#!/usr/bin/env python3

"""
    Exercise 03: Run Timing

    Find the mean of entered timings, terminated by empty input.
    Illustrates basic control flow and a spot of f-string formatting.
"""


def run_timing():
    total_times = 0.0
    counter = 0

    while True:
        new_time = input('Enter 10km Race Time: ')

        if not new_time:
            break
        else:
            try:
                total_times += float(new_time)
                counter += 1
            except ValueError:
                print('Invalid run time entered.')

    print()

    if counter == 0:
        print('No times entered.')
    elif counter == 1:
        print(f'The time of the single run was {total_times:.2f}, but there is no average yet.')
    else:
        print(f'The average time was {total_times / counter:.2f} over {counter} runs.')


if __name__ == '__main__':
    run_timing()
