# Matthew Petersen              03-03-2025
# Lab Week 7

# 



def findSubStringV1(main_str, sub_str):
    return main_str.find(sub_str)

def findSubStringV2(main_str, sub_str):
    return main_str.index(sub_str) if sub_str in main_str else -1

def findSubStringV3(main_str, sub_str):
    len_main, len_sub = len(main_str), len(sub_str)
    
    for i in range(len_main - len_sub + 1):
        if main_str[i:i+len_sub] == sub_str:
            return i
    return -1

def main():
    main_str = input("Enter the main string: ").strip()
    sub_str = input("Enter the substring to search for: ").strip()
    
    result_v1 = findSubStringV1(main_str, sub_str)
    result_v2 = findSubStringV2(main_str, sub_str)
    result_v3 = findSubStringV3(main_str, sub_str)
    
    print(f"Version 1 (.find method): Index {result_v1}")
    print(f"Version 2 (.index method): Index {result_v2}")
    print(f"Version 3 (manual search): Index {result_v3}")

if __name__ == "__main__":
    main()
