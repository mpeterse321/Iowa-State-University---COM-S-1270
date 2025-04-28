# Matthew Petersen
# 3-31-2025
# 
# Description : This code takes a selected text from gutenberg.org and counts how
#  many of each word are in the text. It seperates all words and makes them lowercase.
# 


import string

def analyzeBook(filename):
    count = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                word = word.translate(str.maketrans('', '', string.punctuation))  
                word = word.lower()  
                if word.isalpha():  
                    count[word] = count.get(word, 0) + 1
    return count

def outputAnalysis(count, filename):
    title = filename.replace('.txt', '')
    output_filename = f"{title}_analysis.txt"
    with open(output_filename, 'w', encoding='utf-8') as out:
        for word in sorted(count.keys()):
            out.write(f"{word} {count[word]}\n")
    print(f"Analysis saved to: {output_filename}")

def main():
    filename = input("Enter the filename: ")
    word_counts = analyzeBook(filename)
    outputAnalysis(word_counts, filename)

if __name__ == "__main__":
    main()

