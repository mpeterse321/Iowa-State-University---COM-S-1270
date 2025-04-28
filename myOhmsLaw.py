def calculateVoltage(current, resistance):
    return current * resistance

def main():
    current = float(input("Enter current 'current': "))
    resistance = float(input("Enter resistance 'resistance': "))
    voltage = calculateVoltage(current, resistance)
    print(f"Voltage: {voltage}")

if __name__ == "__main__":
    main()

# _--------------------------------------

def calculateCurrent(voltage, resistance):
    return voltage / resistance

def main():
    voltage = float(input("Enter voltage 'voltage': "))
    resistance = float(input("Enter resistance 'resistance': "))
    current = calculateCurrent(voltage, resistance)
    print(f"Current: {current}")

if __name__ == "__main__":
    main()  

#-------------------------------------------

def calculateResistance(voltage, current):
    return voltage / current

def main():
    voltage = float(input("Enter voltage 'voltage': "))
    current = float(input("Enter current 'current': "))
    resistance = calculateResistance(voltage, current)
    print(f"Resistance: {resistance}")

if __name__ == "__main__":
    main()