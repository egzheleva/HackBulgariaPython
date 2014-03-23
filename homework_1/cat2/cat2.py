import sys
def cat2(*filenames):
    contents = []

    for filename in filenames:
        with open(filename) as file:
            contents.append(file.read())

    return '\n'.join(contents)


if __name__ == '__main__':
    print(cat2(*sys.argv[1:]))