# Matthew Petersen
# Lab 4 
# Description: TCalculating the velocity using acceleration and time with code.

def velocityAccelerationTime(acceleration, time):
    return acceleration * time

def main():
    acceleration = float(input("Enter acceleration 'acceleration': "))
    time = float(input("Enter time 'time': "))
    velocity = velocityAccelerationTime(acceleration, time)
    print(f"Velocity: {velocity}")

if __name__ == "__main__":
    main()