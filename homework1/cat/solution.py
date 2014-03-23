import sys

def cat(filename):
    with open(filename) as file:
        return file.read()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(cat(sys.argv[1]))