def distanceSpeedTime(speed, time):
    return speed * time

def main():
    speed = float(input("Enter speed 'speed': "))
    time = float(input("Enter time 'time': "))
    distance = distanceSpeedTime(speed, time)
    print(f"Distance traveled: {distance} meters")

if __name__ == "__main__":
    main()

# -------------------------------------------------

def velocityAccelerationTime(acceleration, time):
    return acceleration * time

def main():
    acceleration = float(input("Enter acceleration 'acceleration': "))
    time = float(input("Enter time 'time': "))
    velocity = velocityAccelerationTime(acceleration, time)
    print(f"Velocity: {velocity}")

if __name__ == "__main__":
    main()