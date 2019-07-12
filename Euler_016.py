import math



def euler016():
    strPow = str(int(math.pow(2, 1000)))
    res = 0
    for i in range(len(strPow)):
        res += int(strPow[i])

    print("Result : " + str(res))

if __name__ == "__main__":
    euler016()