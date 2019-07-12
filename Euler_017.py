import math



def euler017():
    unit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    decimal = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    res = 0
    for i in range(1, 1001):
        hundredTmp = int((i - i % 100) / 100)
        if (hundredTmp > 0 and hundredTmp < 10):
            res += len(unit[hundredTmp]) + len("hundred")
            if (i % 100 != 0):
                res += len("and")
        elif (hundredTmp == 10):
            res += len("onethousand")
        decimalTmp = i % 100
        if (decimalTmp > 0 and decimalTmp < 20):
            res += len(unit[decimalTmp])
        elif (decimalTmp > 0 and decimalTmp > 19):
            res += len(decimal[int((decimalTmp - (decimalTmp % 10)) / 10)])
            if (decimalTmp % 10 != 0):
                res += len(unit[decimalTmp % 10])
    print (res)

if __name__ == "__main__":
    euler017()