# Matthew Petersen              03-03-2025
# Lab 7
#
#


def reverseStringV1(s):
    return s[::-1]

def main():
    user_input = input("Enter a string to reverse: ")
    
    reversed_string = reverseStringV1(user_input)
    
    print("Reversed string:", reversed_string)

if __name__ == "__main__":
    main()