#4 Write a program to calculate the area of a circle

import math

def area(r):
    return math.pi * r ** 2

if __name__ == '__main__':
    r = int(input('Enter a value for radius(m): '))
    print(str(area(r)) + " (m^2)")


#5 Explore the help() command in python shell