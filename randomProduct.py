# Matthew Petersen          02-10-2025
# Lab 4 
# This code below uses a random number generator to create different outputs in an equation. 
# We are choosing three different variables, a = how many random values we multiply, with b and c = the ranges in which the number is randomly selected. 

import random

def randomProduct(a, b, c):
 
    product = 1
    for _ in range(a):
        random_number = random.randrange(b, c + 1) 
        product *= random_number
    return product

def main():
 
    a = int(input("Enter the number of random values (a): "))
    b = int(input("Enter the lower bound (b): "))
    c = int(input("Enter the upper bound (c): "))
    
    answer = randomProduct(a, b, c)
    
    print("The answer is:", answer)

if __name__ == "__main__":
    main()



