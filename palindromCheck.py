# Matthew Petersen              03-03-2025
# Lab 7
#
# 

from palindromCheck import reverseStringVX 
 
def palindromeCheckV1(user_input):
    reversed_string = reverseStringVX(user_input)
    return user_input == reversed_string

def palindromeCheckV2(user_input):
    length = len(user_input)
    for i in range(length // 2):
        if user_input[i] != user_input[length - 1 - i]:
            return False
    return True

def main():
    user_input = input("Enter a string to check if it's a palindrome: ").strip().lower()
    
    result_v1 = palindromeCheckV1(user_input)
    result_v2 = palindromeCheckV2(user_input)
    
    print(f"Version 1 (using reverseString module): {'Palindrome' if result_v1 else 'Not a palindrome'}")
    print(f"Version 2 (using iterative comparison): {'Palindrome' if result_v2 else 'Not a palindrome'}")

if __name__ == "__main__":
    main()