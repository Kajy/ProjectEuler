import math


def euler022():
    f = open("./ressources/names", "r")
    content = f.read()
    total = 0
    names = sorted(content.replace('\"', '').replace('\n', '').split(','))
    for idx, name in enumerate(names):
        tmp = 0
        for letter in name:
            tmp += ord(letter) - 64

        tmp *= idx + 1
        total += tmp

    print(total)

if __name__ == "__main__":
    euler022()