import math

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    else:
        for x in range(3, round(math.sqrt(n)), 2):
            if n % x == 0:
                return 0
        return 1

def euler003(n):
    for i in range(2, round(math.sqrt(n))):
        if isPrime(i):
            if n % i == 0:
                euler003(n / i)
                break

    print(round(n))
    exit()



if __name__ == "__main__":
    n = 600851475143
    euler003(n)