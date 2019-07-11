import math

def sumUntil(x):
    return int(x * (x + 1) / 2)


def nbDivisorSmallNumber(x):
    nb = 0
    for i in range(1, x +1):
        if (x % i == 0):
            nb += 1
    return nb

def decomposition(x):
    tab = []
    tmp = x
    i = 2
    while tmp > 1:
        if tmp % i == 0:
            tab.append(i)
            tmp /= i
            i = 2
        else:
            i += 1

    uniqueFactor = list(set(tab))
    result = 1
    for i in uniqueFactor:
        result *= nbDivisorSmallNumber(pow(i, tab.count(i)))
    return result

def euler012():
    res = 0
    sum = 1
    while (res < 500):
        sum += 1
        res = decomposition(sumUntil(sum))
    print ("The triangle number " + str(sumUntil(sum)) + " have " + str(res) + " divisor(s)")

if __name__ == "__main__":
    euler012()