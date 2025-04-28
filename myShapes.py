import math


def circleCircumference(radius):
    return 2 * math.pi * radius

def main():
    radius = float(input("Enter the radius of the circle: "))
    circumference = circleCircumference(radius)
    print(f"The circumference of the circle is: {circumference}")

if __name__ == "__main__":
    main()

# -------------------------------------

    import math

def areaOfCircle(radius):
    return math.pi * radius ** 2

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = areaOfCircle(radius)
    print(f"The area of the circle is: {area}")

if __name__ == "__main__":
    main()

    # -------------------------------------
    
def areaOfRectangle(base, height):
    return base * height

def main():
    base = float(input("Enter value 'base': "))
    height = float(input("Enter value 'height': "))
    area = areaOfRectangle(base, height)
    print(f"The area of the Rectangle is: {area}") 

if __name__ == "__main__":
    main()

# -------------------------------------


def rectanglePerimeter (width, height):
    return 2 * (width + height)



def main():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    perimeter = rectanglePerimeter(width, height)
    print(f"The perimeter of the rectangle is: {perimeter}")

if __name__ == "__main__":
    main()
