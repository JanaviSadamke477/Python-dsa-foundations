"""
=========================================================
🐍 DSA Roadmap
Week 2 - Day 3
Topic: Recursion Basics
Author: Janavi Sadmake
=========================================================

Concepts Covered
----------------
✔ Base Case
✔ Recursive Call
✔ Stack Unwinding
✔ Printing Patterns
✔ Mathematical Recursion
✔ Digit Problems

Problems Solved
---------------
1. Print 1 to N
2. Print N to 1
3. Sum of First N Natural Numbers
4. Factorial
5. Power (a^b)
6. Count Digits
7. Sum of Digits
8. Product of Digits
"""

# -------------------------------------------------------
# Q1 Print 1 to N
# -------------------------------------------------------

def print_1_to_n(n):
    if n < 1:
        return

    print_1_to_n(n - 1)
    print(n)

print("Q1")
print_1_to_n(5)

print()


# -------------------------------------------------------
# Q2 Print N to 1
# -------------------------------------------------------

def print_n_to_1(n):
    if n < 1:
        return

    print(n)
    print_n_to_1(n - 1)

print("Q2")
print_n_to_1(5)

print()


# -------------------------------------------------------
# Q3 Sum of First N Numbers
# -------------------------------------------------------

def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)

print("Q3")
print(sum_n(5))

print()


# -------------------------------------------------------
# Q4 Factorial
# -------------------------------------------------------

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print("Q4")
print(factorial(5))

print()


# -------------------------------------------------------
# Q5 Power
# -------------------------------------------------------

def power(a, b):
    if b == 0:
        return 1

    return a * power(a, b - 1)

print("Q5")
print(power(5, 3))

print()


# -------------------------------------------------------
# Q6 Count Digits
# -------------------------------------------------------

def count_digits(n):
    if n == 0:
        return 0

    return 1 + count_digits(n // 10)

print("Q6")
print(count_digits(12345))

print()


# -------------------------------------------------------
# Q7 Sum of Digits
# -------------------------------------------------------

def sum_digits(n):
    if n == 0:
        return 0

    digit = n % 10

    return digit + sum_digits(n // 10)

print("Q7")
print(sum_digits(12345))

print()


# -------------------------------------------------------
# Q8 Product of Digits
# -------------------------------------------------------

def product_digits(n):
    if n == 0:
        return 1

    digit = n % 10

    return digit * product_digits(n // 10)

print("Q8")
print(product_digits(123))

print()
