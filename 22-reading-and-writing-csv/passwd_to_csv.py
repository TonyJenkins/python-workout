#!/usr/bin/env python3

"""
    Exercise 22: Passwd to CSV

    Process a Un*x passwd file, writing out a corresponding tab-separated CSV.
        Note that line terminators differ between OSs. The hack on opening the output
        CSV is needed for Windows.
"""


import csv


def passwd_to_csv(passwd_file, csv_file):

    with open(passwd_file) as passwd, open(csv_file, 'w', newline='') as csv_file:

        csv_out = csv.writer(csv_file, delimiter='\t')

        for line in passwd:
            if not line.startswith(('#', '\n')):
                record = line.split(':')
                csv_out.writerow((record[0], record[2]))


if __name__ == '__main__':

    passwd_to_csv('passwd.txt', 'passwd.csv')
