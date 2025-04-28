# Matthew Petersen              03-03-2025
# Lab week 7

# Making a tridecagon system through using a turtle to draw a tridecagon 

import turtle
import random
import tridecagonLSystem


def applyRules(ch):
    """Applies transformation rules to generate new L-system commands."""
    if ch == 'F':
        return "F-F++F-FH"
    elif ch == 'H':
        return "HFP"
    elif ch == 'P':
        return "PF-F"
    else:
        return ch

def processString(oldStr):
    """Generates new L-system string based on rules."""
    newStr = ""
    for ch in oldStr:
        newStr += applyRules(ch)
    return newStr

def createLSystem(numIters, axiom):
    """Generates the final L-system string after given iterations."""
    startString = axiom
    for _ in range(numIters):
        startString = processString(startString)
    return startString

def drawLsystem(aTurtle, instructions, angle, distance):
    """Draws the L-system using turtle graphics."""
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == 'H':
            tridecagonTurtle(aTurtle)  # Draw a tridecagon
        elif cmd == 'P':
            aTurtle.penup()
            aTurtle.goto(random.randint(-200, 200), random.randint(-200, 200))
            aTurtle.pendown()

def main():
    """Main function to execute the L-system drawing."""
    wn = turtle.Screen()
    wn.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    
    axiom = "F"
    numIterations = 4
    angle = random.randint(60, 90)  
    distance = 10
    
    instructions = createLSystem(numIterations, axiom)
    print("L-system instructions:", instructions)
    
    drawLsystem(t, instructions, angle, distance)
    
    wn.mainloop()

if __name__ == "__main__":
    main()
