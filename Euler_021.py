import math

def getSumAllDivisor(nb):
    sum = 0
    for i in range(1, int(nb / 2) + 1):
        if nb % i == 0:
            sum += i

    return sum

def checkAmicable(nb):
    sum = getSumAllDivisor(nb)
    return getSumAllDivisor(sum) == nb and nb != sum

def euler021():
    amicables = []
    for i in range(1, 10000):
        if checkAmicable(i):
            amicables.append(i)

    print(amicables)
    print(sum(amicables))

if __name__ == "__main__":
    euler021()