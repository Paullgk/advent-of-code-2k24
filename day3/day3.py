import re

if __name__ == '__main__':
    f = open("day3/example", "r")
    data = f.read()
    occurences = re.finditer(r"mul\(", data)

    for occurence in occurences:

        pass
    