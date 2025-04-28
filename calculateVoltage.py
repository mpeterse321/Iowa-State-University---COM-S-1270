# Matthew Petersen
# Lab 4 
# Description: Calculateing voltage using code.

def calculateVoltage(current, resistance):
    return current * resistance

def main():
    current = float(input("Enter current 'current': "))
    resistance = float(input("Enter resistance 'resistance': "))
    voltage = calculateVoltage(current, resistance)
    print(f"Voltage: {voltage}")

if __name__ == "__main__":
    main()