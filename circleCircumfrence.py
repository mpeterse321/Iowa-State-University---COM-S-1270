# Matthew Petersen
# Lab 4 
# Description: Finding the circumference of a circle using code.

import math


def circleCircumference(radius):
    return 2 * math.pi * radius

def main():
    radius = float(input("Enter the radius of the circle: "))
    circumference = circleCircumference(radius)
    print(f"The circumference of the circle is: {circumference}")

if __name__ == "__main__":
    main()