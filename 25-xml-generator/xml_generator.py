#!/usr/bin/env python3

"""
    Exercise 25: XML Generator

    Use a function to generate simple XML.
        Illustrates variable function paramaters.
"""


def myxml(tag, content='', **kwargs):

    attributes = ''
    for key, value in kwargs.items():
        attributes += f' {key}="{value}"'

    return f'<{tag}{attributes.rstrip()}>{content}</{tag}>'


if __name__ == '__main__':
    print(myxml('foo'))
    print(myxml('foo', 'bar'))
    print(myxml('foo', 'bar', a=1, b=2, c=3))
