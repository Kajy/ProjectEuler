import math


def searchPath(size):
    paths = [[0 for x in range(size)] for y in range(size)]
    for x in range(size):
        for y in range(size):
            if x == 0 or y == 0:
                paths[x][y] = 1
            else:
                paths[x][y] = paths[x - 1][y] + paths[x][y - 1]

    return paths

def euler015():
    gridSize = 20
    print (searchPath(gridSize + 1)[gridSize][gridSize])

if __name__ == "__main__":
    euler015()