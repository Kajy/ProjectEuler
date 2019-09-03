import math

# 0 = Monday
# 1 = Tuesday
# 2 = Wednesday
# 3 = Thursday
# 4 = Friday
# 5 = Saturday
# 6 = Sunday

def isLeapYear(year):
   return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def daysInYear(year):
    if isLeapYear(year):
        return 366
    else:
        return 365

def processYear(startDay, isLeap):

    calendar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    currentDay = startDay
    goodSunday = 0
    for i in range(1, 13):
        if (currentDay % 7 == 6):
            goodSunday += 1
           # print("Good Sunday of month " + str(i))
        if (i == 2):
            currentDay += calendar[i] + isLeap
        else:
            currentDay += calendar[i]
    return goodSunday

def euler019():
    prevStart = 0 # 1900 start a Monday
    total = 0
    for i in range(1901, 2001):
        prevStart = (daysInYear(i - 1) + prevStart) % 7
       # print("Start the " + str(prevStart + 1) + "th day of the week")
        print("For the year " + str(i) + " there are " + str(processYear(prevStart, isLeapYear(i))) + " Sundays who started a month")
        total += processYear(prevStart, isLeapYear(i))
    print("Total sundays : " + str(total))

if __name__ == "__main__":
    euler019()