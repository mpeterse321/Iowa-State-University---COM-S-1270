# Matthew Petersen          02-24-2025
# Lab 6

# We are creating a multiplication table using code

def multiplicationTable(lowNum, highNum):
    print("", end="")
    for i in range(lowNum, highNum + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * ((highNum - lowNum + 1) * 4 + 3))

    for i in range(lowNum, highNum + 1):
        print(f"{i:<3}|", end="")  
        for j in range(lowNum, highNum + 1):
            print(f"{i * j:4}", end="")  
        print()  

def main():
    lowNum = int(input("Enter the lower bound of the multiplication table: "))
    highNum = int(input("Enter the upper bound of the multiplication table: "))

    multiplicationTable(lowNum, highNum)

if __name__ == "__main__":
    main()
