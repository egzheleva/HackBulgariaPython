import sys

def sum_numbers(filename):
    with open(filename) as file:
        return sum(map(int, file.read().split()))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sum_numbers(sys.argv[1]))