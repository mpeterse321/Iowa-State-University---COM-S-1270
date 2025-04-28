# Matthew Petersen
# 3-24-2025
# Lab week 10
# 
# Description : This code randomly generates a list that is inbetweem 1 - 2000
# and then genreate a mean and median of the list and prints its results.


import random

def generateInput():
    length = random.randint(200, 500)  
    return [random.randint(1, 2000) for _ in range(length)] 

def findMean(numbers):
    total = 0
    count = len(numbers)
    for num in numbers:
        total += num  
    return total / count if count > 0 else 0

def findMedian(numbers):
    numbers.sort()  
    length = len(numbers)
    mid = length // 2
    if length % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2  
    else:
        return numbers[mid]  

def main():
    numList = generateInput()
    mean = findMean(numList)
    median = findMedian(numList)
    print("Mean: {0} Median: {1}".format(mean, median))

if __name__ == "__main__":
    main()

