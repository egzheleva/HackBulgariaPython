import sys

def wc(command, filename):
    with open(filename) as file:
        contents = file.read()

    if command == 'chars':
        return len(contents)
    elif command == 'words':
        return len(contents.split())
    elif command == 'lines':
        return len(contents.split('\n'))


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print(wc(*sys.argv[1:3]))