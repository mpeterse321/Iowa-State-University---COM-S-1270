# Matthew Petersen 
# Lab 4
# Code conversion: Take all of the code equations from last week and but them into one system where we can use any 
# equation without switching from code to code. We made a calculator to understand all equations.


import myShapes
import myFinances
import myOhmsLaw
import myPhysics


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

def main():
    print("Welcome to the Calculation Test Program!")
    running = True

    while running:
        print("\nChoose a calculation category:")
        print("1. Shapes")
        print("2. Physics")
        print("3. Ohm's Law")
        print("4. Finances")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\nShapes Calculations:")
            print("a. Area of Rectangle")
            print("b. Perimeter of Rectangle")
            print("c. Area of Circle")
            print("d. Circumference of Circle")

            shape_choice = input("Choose an option (a-d): ").strip().lower()

            if shape_choice == "a":
                length = get_float_input("Enter length: ")
                width = get_float_input("Enter width: ")
                print(f"Area of Rectangle: {myShapes.areaOfRectangle(length, width)}")
            elif shape_choice == "b":
                length = get_float_input("Enter length: ")
                width = get_float_input("Enter width: ")
                print(f"Rectangle Perimeter: {myShapes.rectanglePerimeter(length, width)}")
            elif shape_choice == "c":
                radius = get_float_input("Enter radius: ")
                print(f"Area of Circle: {myShapes.areaOfCircle(radius)}")
            elif shape_choice == "d":
                radius = get_float_input("Enter radius: ")
                print(f"Circle Circumference: {myShapes.circleCircumference(radius)}")

        elif choice == "2":
            print("\nPhysics Calculations:")
            print("a. Distance = Speed * Time")
            print("b. Velocity = Initial Velocity + Acceleration * Time")

            physics_choice = input("Choose an option (a-b): ").strip().lower()

            if physics_choice == "a":
                speed = get_float_input("Enter speed: ")
                time = get_float_input("Enter time: ")
                print(f"Distance: {myPhysics.distanceSpeedTime(speed, time)}")
            elif physics_choice == "b":
                initial_velocity = get_float_input("Enter initial velocity: ")
                acceleration = get_float_input("Enter acceleration: ")
                time = get_float_input("Enter time: ")
                print(f"Velocity: {myPhysics.velocityAccelerationTime(initial_velocity, acceleration, time)}")

        elif choice == "3":
            print("\nOhm's Law Calculations:")
            print("a. Voltage = Current * Resistance")
            print("b. Resistance = Voltage / Current")
            print("c. Current = Voltage / Resistance")

            ohm_choice = input("Choose an option (a-c): ").strip().lower()

            if ohm_choice == "a":
                current = get_float_input("Enter current: ")
                resistance = get_float_input("Enter resistance: ")
                print(f"Voltage: {myOhmsLaw.calculateVoltage(current, resistance)}")
            elif ohm_choice == "b":
                voltage = get_float_input("Enter voltage: ")
                current = get_float_input("Enter current: ")
                print(f"Resistance: {myOhmsLaw.calculateResistance(voltage, current)}")
            elif ohm_choice == "c":
                voltage = get_float_input("Enter voltage: ")
                resistance = get_float_input("Enter resistance: ")
                print(f"Current: {myOhmsLaw.calculateCurrent(voltage, resistance)}")
            

        elif choice == "4":
            print("\nFinance Calculations:")
            print("a. Annual Percentage Rate")
            print("b. Compound Amount")

            finance_choice = input("Choose an option (a-b): ").strip().lower()

            if finance_choice == "a":
                principal = get_float_input("Enter principal amount: ")
                rate = get_float_input("Enter annual interest rate (%): ")
                time = get_float_input("Enter time in years: ")
                print(f"Total Amount: {myFinances.annualPercentageRate(principal, rate, time)}")
            elif finance_choice == "b":
                principal = get_float_input("Enter principal amount: ")
                rate = get_float_input("Enter annual interest rate (%): ")
                time = get_float_input("Enter time in years: ")
                n = get_float_input("Enter number of times interest is compounded per year: ")
                print(f"Total Compound Amount: {myFinances.compoundAmount(principal, rate, time, n)}")

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            running = False

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

