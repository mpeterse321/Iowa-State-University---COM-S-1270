# Matthew Petersen          02-17-2025
# Lab week 5 
# The purpose of this script is to create a new function which draws multiple tridecagons in a line - one after the other. It will do this
# by calling your original tridecagon-drawing function multiple times in a loop

import turtle

def tridecagonTurtle(s, x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    for _ in range(13):
        t.forward(s)
        t.left(360 / 13)

def drawMultipleTridecagons(s, x, y, nr, sr, t):
    for i in range(nr):
        tridecagonTurtle(s, x + (i * sr), y, t)

def main():
    s = int(input("Enter the side length of the tridecagon: "))
    x = int(input("Enter the starting x-coordinate: "))
    y = int(input("Enter the starting y-coordinate: "))
    nr = int(input("Enter the number of tridecagons to draw: "))
    sr = int(input("Enter the spacing between tridecagons: "))

    screen = turtle.Screen()
    t = turtle.Turtle()
    
    drawMultipleTridecagons(s, x, y, nr, sr, t)
    
    screen.mainloop()
if __name__ == "__main__":
    main()
