#!/usr/bin/env python3

"""
    Additional: Shell Count (Exercise 18)

    Use a password file to count up the shells used on a system.
"""


def count_shells(passwd):

    shells = {}

    with open(passwd) as p:
        for line in p:
            if line.startswith('#') or line.startswith('\n'):
                continue
            else:
                this_shell = line.split(':')[9][:-1]
                if this_shell in shells.keys():
                    shells[this_shell] += 1
                else:
                    shells[this_shell] = 1

    return shells


if __name__ == '__main__':

    print(count_shells('passwd.txt'))


