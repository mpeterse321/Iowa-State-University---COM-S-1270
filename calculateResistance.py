# Matthew Petersen
# Lab 4 
# Description: Calculateing the resistance using code.

def calculateResistance(voltage, current):
    return voltage / current

def main():
    voltage = float(input("Enter voltage 'voltage': "))
    current = float(input("Enter current 'current': "))
    resistance = calculateResistance(voltage, current)
    print(f"Resistance: {resistance}")

if __name__ == "__main__":
    main()