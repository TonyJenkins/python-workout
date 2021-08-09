#!/usr/bin/env python3

"""
    Exercise 23: JSON

    Process JSON files to summarise student test results.
"""


from glob import glob
import json


def print_scores(folder):

    scores = {}

    for filename in glob(f'{folder}/*.json'):

        scores[filename] = {}

        with open(filename) as results:
            for result in json.load(results):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)

    for the_class in scores:
        print(the_class)
        print('=' * len(the_class))
        print()

        for subject, subject_scores in scores[the_class].items():
            print(subject.capitalize())
            print(f'    Max Score: {max(subject_scores)}')
            print(f'    Min Score: {min(subject_scores)}')
            print(f'    Avg Score: {sum(subject_scores) / len(subject_scores)}')
            print()


if __name__ == '__main__':

    print_scores('scores')
