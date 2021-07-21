#!/usr/bin/env python3

def pig_latin(word):

    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'way'

