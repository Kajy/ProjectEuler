import math


def collatzSequence(x):
    len = 0
    while x != 1:
        if x % 2 == 1:
            x = x * 3 + 1
        else:
            x /= 2
        len += 1
    return len

def euler014():
    len = 0
    res = 0
    for nb in range(1, 1000000):
        tmpLen = collatzSequence(nb)
        if tmpLen > len:
            len = tmpLen
            res = nb

    print ("The number " + str(res) + " have the longest chain of " + str(len))


if __name__ == "__main__":
    euler014()