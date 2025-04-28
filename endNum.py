# Matthew Petersen 
# 3-24-2025
# Lab week 10
# 
# Description: This code will take the list that you enetered and outpout a list 
# that puts the numeric integer at the end of the list.

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter an integer (* to stop): ")
        if user_input == "*":
            break
        numbers.append(int(user_input)) 
    return numbers

def endNum(intList, num):
    non_target = [x for x in intList if x != num] 
    target = [x for x in intList if x == num]
    return non_target + target  

def main():
    intList = get_numbers()
    num = int(input("Enter the number to move to the end: "))
    print(f"Updated list: {endNum(intList, num)}")

if __name__ == "__main__":
    main()

