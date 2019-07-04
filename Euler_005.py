def euler005():
    for n in range(20, 1000000000, 20):
        if (n % 3 == 0 and n % 6 == 0 and n % 7 == 0 and n % 8 == 0 and n % 9 == 0 and n % 11 == 0 and n % 12 == 0 and
                n % 13 == 0 and n % 14 == 0 and n % 15 == 0 and n % 16 == 0 and n % 17 == 0 and n % 18 == 0 and n % 19 == 0):
                print(n)
                break



if __name__ == "__main__":
    euler005()