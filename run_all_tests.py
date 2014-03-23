import os
import fnmatch
from subprocess import call


def find_all_test_files(directory):
    matches = []

    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, 'tests.py'):
            matches.append(os.path.join(root, filename))

    return matches


if __name__ == '__main__':
    for test_file in find_all_test_files('Homework1'):
        call(['python3', test_file]
