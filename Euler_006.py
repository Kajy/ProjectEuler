import math

def euler006():
    n1 = 0
    n2 = 0
    for x in range(1, 101):
        n1 += math.pow(x, 2)
        n2 += x
    print(round(math.pow(n2, 2) - n1))



if __name__ == "__main__":
    euler006()