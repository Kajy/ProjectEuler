import math

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    else:
        for x in range(3, round(math.sqrt(n)) + 1, 2):
            if n % x == 0:
                return 0
        return 1

def euler007():
    n = 0
    for i in range(2, 10001 * 10001, 1):
        if isPrime(i):
            n += 1
        if n == 10001:
            print(i)
            break


if __name__ == "__main__":
    euler007()