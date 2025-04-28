# Matthew Petersen
# 3-31-2025
# 
# 
# Description : This code creates a new cleansed text of a certain text inputed into the code.
# 



def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def removeNonASCII(text):
    clean = "".join(char for char in text if ord(char) < 128)
    return clean

def write_clean_file(original_filename, clean_text):
    new_filename = original_filename.replace('.txt', '_clean.txt')
    with open(new_filename, 'w', encoding='utf-8') as file:
        file.write(clean_text)
    print(f"Cleaned file saved as: {new_filename}")

def main():
    filename = input("Enter the filename: ")
    file_content = read_file(filename)
    clean_content = removeNonASCII(file_content)
    write_clean_file(filename, clean_content)

if __name__ == "__main__":
    main()