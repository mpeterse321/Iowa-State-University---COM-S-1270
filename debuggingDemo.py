# Matthew Petersen           02-10-2025
# Lab Week 4: 
# Description: Debugging Bemo - chosen from my scrpit areaOfRectangle

import pdb
def areaOfRectangle(base, height):

    return base * height

def main():
    base = float(input("Enter value 'base': "))
    height = float(input("Enter value 'height': "))
    area = areaOfRectangle(base, height)
    print(f"The area of the Rectangle is: {area} ")

if __name__ == "__main__":
    main()



