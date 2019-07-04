import math

def euler003(n):
    for i in range(2, round(math.sqrt(n))):
            if n % i == 0:
                euler003(n / i)
                break
    print(round(n))
    exit()



if __name__ == "__main__":
    n = 600851475143
    euler003(n)