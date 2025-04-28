# Matthew Petersen         
# Lab 4 
# Discription: finding the perimeter of a rectangle using code

def rectanglePerimeter (width, height):
    return 2 * (width + height)

def main():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    perimeter = rectanglePerimeter(width, height)
    print(f"The perimeter of the rectangle is: {perimeter}")

if __name__ == "__main__":
    main()