# Matthew Petersen          02-24-2025
# Lab 6
# This program prompts the user for an integer input and prints a right triangle pattern of stars with the given number of row

def starRightTriangle(num):
    for i in range(1, num + 1):
        print('*' * i)

def main():
    num = int(input("Enter an integer: "))
    starRightTriangle(num)

if __name__ == "__main__":
    main()