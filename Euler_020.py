import math


def euler020():
    number = str(math.factorial(100))
    sum = 0
    for i in number:
        sum += int(i)
    print (sum)

if __name__ == "__main__":
    euler020()