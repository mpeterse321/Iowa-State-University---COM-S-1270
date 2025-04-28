# Matthew Petersen
#  4-7-2025
# Lab Week 12
# 
# Description : This code is supposed to test all mathmatical functions from the myMath.py code 
# which all had differnet errors in the code. This code determines the errors in those functions
# and tests them.

import pytest
from myMath import *

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(4, 0.5) == 2

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(13)

def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits(1001) == 2

def test_gcd():
    assert gcd(20, 8) == 4
    assert gcd(17, 13) == 1
    assert gcd(54, 24) == 6


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(5) == 5
    assert fib(10) == 55

def test_lcm():
    assert lcm(6, 8) == 24
    assert lcm(3, 7) == 21

def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(2) == 2 ** 0.5

def test_abs_diff():
    assert abs_diff(5, 3) == 2
    assert abs_diff(3, 5) == 2
    assert abs_diff(7, 7) == 0

def test_log():
    import math
    assert log(100, 10) == math.log(100, 10)
    assert log(8, 2) == 3
    with pytest.raises(ValueError):
        log(-10)

def test_mod():
    assert mod(10, 3) == 1
    assert mod(20, 5) == 0
    assert mod(-7, 4) == -7 % 4

def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3
    assert mean([5, 5, 5, 5]) == 5
    assert mean([0, 10]) == 5

def test_median():
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([4, 1, 3, 2]) == 2.5

def test_mode():
    assert mode([1, 2, 2, 3]) == 2
    assert mode([5, 5, 5, 2]) == 5

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(-40) == -40

def test_inverse():
    assert inverse(2) == 0.5
    assert inverse(-4) == -0.25
    with pytest.raises(ZeroDivisionError):
        inverse(0)

def test_triangular_number():
    assert triangular_number(1) == 1
    assert triangular_number(3) == 6
    assert triangular_number(7) == 28