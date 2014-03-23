import sys
import random

def generate_numbers(filename, n):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, random.sample(range(1000), n))))


if __name__ == '__main__':
    if len(sys.argv) > 2:
        generate_numbers(*sys.argv[1:3])