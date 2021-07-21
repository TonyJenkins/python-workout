#!/usr/bin/env python3

"""
    Exercise 06: Pig Latin Sentence

    Convert a complete sentence into a "Pig Latin" sentence using
    the function from exercise 05.

"""

from pig_latin import pig_latin


def pig_latin_sentence(sentence):
    words = []

    for each_word in sentence.split():
        words.append(pig_latin(each_word))

    return ' '.join(words)


if __name__ == '__main__':

    while True:
        s = input('Enter a sentence to be converted: ')

        if not s:
            break
        else:
            print(pig_latin_sentence(s))
