def isPalindrome(n):
    return (int(str(n)[::-1]) == n)

def euler004():
    res = 42
    for x in range(100, 1000):
        for y in range(100, 1000):
            if isPalindrome(x * y):
                if (x * y > res):
                    res = x * y

    print(res)

if __name__ == "__main__":
    euler004()