def euler002():
    n1 = 1
    n2 = 2
    res = 0
    while (n1 < 4000000):
        if (n1 % 2 == 0):
            res += n1
        tmp = n2
        n2 += n1
        n1 = tmp
    print(res)


if __name__ == "__main__":
    euler002()