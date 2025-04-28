# Matthew Petersen          02-10-2025
# lab 4 
# Create a tridecagon using a turtle 

import turtle

def tridecagonTurtle(s, x, y, t):
    
    t.penup()
    t.goto(x, y)
    t.pendown()

    angle = 360 / 13    

    for _ in range(13):
        t.forward(s)
        t.right(angle)

def main():
    s = int(input("Enter the length of one of the sides of the regular tridecagon:"))
    x = int(input("Enter the X-coordanite of the tridecagons vertex: "))
    y = int(input("Enter the Y-coordanite of the tridecagons vertex"))

    t = turtle.Turtle()
    t.pensize(3)

    tridecagonTurtle(s, x, y, t)

    turtle.done()

__name__ == "__main__"
main()
