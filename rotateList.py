# Matthew Petersen 
# 3-24-2025
# Lab week 10
# 
# Description: This code will take the list that you enetered and depending 
# on the number of rotations entered the code will rotate the numbers that many times.

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter an integer (* to stop): ")
        if user_input == "*":
            break
        numbers.append(int(user_input))  
    return numbers

def rotateList(intList, rot):
    if not intList:
        return intList  
    rot = rot % len(intList) 
    return intList[-rot:] + intList[:-rot] if rot else intList

def main():
    intList = get_numbers()
    rot = int(input("Enter the number of positions to rotate: "))
    print(f"Rotated list: {rotateList(intList, rot)}")

if __name__ == "__main__":
    main()
