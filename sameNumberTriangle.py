# Matthew Petersen              02-24-2025
# lab 6
# Use code to insert an integer to create a right triangle with all of the same numbers on the same rows.pytho

def sameNumberTriangle(num):
    for i in range(1, num + 1):
        print(' '.join(str(i) for _ in range(i)))

def main():
    num = int(input("Enter an integer: "))
    sameNumberTriangle(num)

if __name__ == "__main__":
    main()