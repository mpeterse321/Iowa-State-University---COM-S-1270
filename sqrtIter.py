# Matthew Petersen          02-10-2025
# Lab 4
#


def sqrtIter(x, iterations):
    y = (x + 1) / 2
    
    for _ in range(iterations):
       y = ((x / y) + y) / 2
    return y 

def main():
     x = int(input("Enter a value for x to find the square root of: "))
     iterations = int(input("Enter the number of iterations:"))

     answer = sqrtIter(x, iterations)

     print("The answer is", [answer])


if __name__ == "__main__":
    main()








