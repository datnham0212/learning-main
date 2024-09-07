import math
def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 366
    else:
        return 365

def calculateMinutes(year):
    return year * 24 * 60

def lightYear(year):
    return year * 365 * 24 * 60 * 3 * pow(10, 8)

if __name__ == "__main__":
    year = isLeapYear(int(input("Enter a year: ")))
    print(calculateMinutes(year))
    print(lightYear(year))