#!/usr/bin/env python3

"""
    Additional: Log File Analyser (Exercise 21)

    Process an HTTP log file and report distribution of response codes.

"""


def analyse_log(logfile):

    codes = {}
    lines = 0

    with open(logfile) as log:
        for line in log:
            lines += 1
            code = line.split(' ')[8]
            if code in codes.keys():
                codes[code] += 1
            else:
                codes[code] = 1

    print(f'Accesses: {lines}')
    print()

    for code in sorted(codes):
        print(f'Code {code}: {codes[code]:-5} ({codes[code]/lines*100:5.2f}%)')


if __name__ == '__main__':
    analyse_log('access.log')
