# Matthew Petersen
# Lab 4 
# Description: Calculating the distance using speed and time with code.

def distanceSpeedTime(speed, time):
    return speed * time

def main():
    speed = float(input("Enter speed 'speed': "))
    time = float(input("Enter time 'time': "))
    distance = distanceSpeedTime(speed, time)
    print(f"Distance traveled: {distance} meters")

if __name__ == "__main__":
    main()