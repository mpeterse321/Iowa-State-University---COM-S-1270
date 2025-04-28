# Matthew Petersen
# 3-24-2025
# Lab week 10
# 
# Description : This code determines if the strings entered into the code 
# will result in a palindomic by printing true or false. The code is stopped
# when * is enterd into the input. 
# 


def get_strings():
    strings = []
    while True:
        user_input = input("Enter a string (* to stop): ")
        if user_input == "*":
            break
        strings.append(user_input)  
    return strings

def palindromeList(lst):
    length = len(lst)
    for i in range(length // 2): 
        if lst[i] != lst[length - 1 - i]:
            return False
    return True

def main():
    palList = get_strings()
    if palList:
        print(f"Is the list palindromic? {palindromeList(palList)}")
    else:
        print("No strings were entered.")

if __name__ == "__main__":
    main()


