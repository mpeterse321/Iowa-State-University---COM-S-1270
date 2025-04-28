# Matthew Petersen              02-24-2025
# lab 6
# use integer input to print a number pyramid pattern with the given number of rows.

def numberDiamond(num):
    for i in range(1, num + 1):
        spaces = ' ' * (num - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        print(spaces + numbers)
    
    for i in range(num - 1, 0, -1):
        spaces = ' ' * (num - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        print(spaces + numbers)

def main():
    num = int(input("Enter an integer: "))
    numberDiamond(num)

if __name__ == "__main__":
    main()