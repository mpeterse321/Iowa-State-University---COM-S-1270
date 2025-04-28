# A module containing a variety of mathematical operators
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(base, exponent):
    return base ** exponent

def factorial(n):
    if n < 0:
        raise ValueError("Input cannot be negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):  # Optimized to check only up to √n
        if n % i == 0:
            return False
    
    return True

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def fib(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def square_root(n):
    return n ** 0.5

def abs_diff(a, b):
    return abs(a - b)

def log(a, base=10):
    import math
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    
    return math.log(a, base)


def mod(a, b):
    return a % b

def mean(numbers):
    return sum(numbers) / len(numbers)
def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    return sorted_numbers[n//2]

def mode(numbers):
    from collections import Counter
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def inverse(a):
    return 1 / a

def triangular_number(n):
    return n * (n + 1) // 2
