import math

def euler009():

    for a in range (1, 333): # can't be > 332
        for b in range (a, 498): # can't be > 498
            c = math.sqrt(a * a + b * b)
            if a + b + c == 1000:
                print(round(a * b * c))


if __name__ == "__main__":
    euler009()