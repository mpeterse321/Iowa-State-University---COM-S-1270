# Matthew Petersen 
# 3-24-2025
# Lab week 10
# 
# Description: In this code we enter as many numeric integers as we want 
# while using * to stop the numbers. Then the code takes the max number 
# and the minimum nuber of the integers entered into the code.


def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter an integer (* to stop): ")
        if user_input == "*":
            break
        numbers.append(user_input) 
    return [int(num) for num in numbers] 

def findMin(numbers):
    if not numbers:
        return None 
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

def findMax(numbers):
    if not numbers:
        return None  
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

def main():
    numbers = get_numbers()
    if numbers:
        print(f"Minimum value: {findMin(numbers)}")
        print(f"Maximum value: {findMax(numbers)}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()

