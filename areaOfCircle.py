# Matthew Petersen          02-10-2025
# Lab 4
# Description: Finding the area of a circle using code.

import math

def areaOfCircle(radius):
    return math.pi * radius ** 2

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = areaOfCircle(radius)
    print(f"The area of the circle is: {area}")

if __name__ == "__main__":
    main()