# Matthew Petersen
# 3-31-2025
# 
# Description : This code take a sentence which is inputed into the code 
# and mixes the words around randomly to create another jumbled up sentence.
# 


import random

def swap_words(sentence):
    words = sentence.split()
    unique_words = list(set(words))  
    shuffled_words = unique_words[:]
    random.shuffle(shuffled_words)  
    
    swap_dict = {key: value for key, value in zip(unique_words, shuffled_words)}
    
    swapped_sentence = " ".join(swap_dict[word] for word in words)
    
    return swap_dict, swapped_sentence

def main():
    sentence = input("Enter a sentence: ")
    swap_dict, swapped_sentence = swap_words(sentence)
    
    print("\nWord Swap Dictionary:")
    for key, value in swap_dict.items():
        print(f"{key} -> {value}")
    
    print("\nSwapped Sentence:")
    print(swapped_sentence)

if __name__ == "__main__":
    main()
