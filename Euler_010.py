import math

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    else:
        for x in range(3, round(math.sqrt(n)) + 1, 2):
            if n % x == 0:
                return 0
        return 1

def euler010():
    res = 2
    for x in range(3, 2000000, 2):
        if isPrime(x):
            res += x
    print(res)


if __name__ == "__main__":
    euler010()