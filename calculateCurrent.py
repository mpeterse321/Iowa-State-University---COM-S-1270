# Matthew Petersen
# Lab 4 
# Description: Calculating current using code.

def calculateCurrent(voltage, resistance):
    return voltage / resistance

def main():
    voltage = float(input("Enter voltage 'voltage': "))
    resistance = float(input("Enter resistance 'resistance': "))
    current = calculateCurrent(voltage, resistance)
    print(f"Current: {current}")

if __name__ == "__main__":
    main()