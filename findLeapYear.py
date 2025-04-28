# Matthew Petersen          02-17-2025
# Lab week 5 
# We will calculate whether the specified year is a leap year or not using code


def findLeapYear(year):
    """Determines if a given year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    """Main function to take user input and check if it's a leap year."""
    year = int(input("Enter a year: "))
    answer = findLeapYear(year)
    
    # Print result
    if answer:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
