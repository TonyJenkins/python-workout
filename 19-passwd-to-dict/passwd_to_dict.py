#!/usr/bin/env python3

"""
    Exercise 19: /etc/passwd to Dict

    Process a Un*x password file into a dictionary.
"""


def passwd_to_dict(passwd):

    users = {}

    with open(passwd) as p:
        for line in p:
            if line.startswith('#') or line.startswith('\n'):
                continue
            else:
                user = line.split(':')
                users[user[0]] = user[2]

    return users


if __name__ == '__main__':

    print(passwd_to_dict('passwd.txt'))
