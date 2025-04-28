import turtle

def tridecagonTurtle(s, x, y, t):
    """
    Draws a regular tridecagon (13-sided polygon) using the Turtle graphics library.
    
    Parameters:
    s (int): Side length of the tridecagon.
    x (int): X-coordinate of the starting vertex.
    y (int): Y-coordinate of the starting vertex.
    t (Turtle): The turtle object used for drawing.
    
    Reference for tridecagon angles: 
    - A regular tridecagon has exterior angles of approximately 27.69 degrees.
    - Source: https://en.wikipedia.org/wiki/Tridecagon
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    angle = 360 / 13  # Each exterior angle in a regular tridecagon
    
    for _ in range(13):
        t.forward(s)
        t.right(angle)

def main():
    # Prompting user input
    s = int(input("Enter the side length of the tridecagon: "))
    x = int(input("Enter the x-coordinate of the starting vertex: "))
    y = int(input("Enter the y-coordinate of the starting vertex: "))
    
    # Creating the turtle object
    t = turtle.Turtle()
    t.speed(3)  # Setting turtle speed
    
    # Draw the tridecagon
    tridecagonTurtle(s, x, y, t)
    
    # Keep the window open
    turtle.done()

if __name__ == "__main__":
    main()
