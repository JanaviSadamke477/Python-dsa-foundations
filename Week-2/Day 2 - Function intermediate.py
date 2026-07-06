# =================================================================
# Week 2 - Day 2 : Intermediate Functions
# Date: 07 July 2026
# =================================================================


# Q1 - Return Maximum of Two Numbers

def maximum(a, b):

    if a > b:
        return a

    else:
        return b

result = maximum(10, 12)
print(result)

print()


# Q2 - Return Minimum of Two Numbers

def minimum(a, b):

    if a > b:
        return b

    else:
        return a

result = minimum(10, 12)
print(result)

print()


# Q3 - Return Absolute Difference

def difference(a, b):

    return abs(a - b)

result = difference(12, 56)
print(result)

print()


# Q4 - Return Average of Three Numbers

def average(a, b, c):

    avg = (a + b + c) / 3

    return avg

result = average(34, 65, 78)
print(result)

print()


# Q5 - Return Sum of First n Natural Numbers

def sum_n(n):

    total = 0

    for i in range(1, n + 1):
        total += i

    return total

result = sum_n(10)
print(result)

print()


# Q6 - Sum of Squares using Function Calling Function

def square(n):
    return n * n

def sum_of_squares(a, b):

    return square(a) + square(b)

result = sum_of_squares(4, 6)
print(result)

print()


# Q7 - Sum of Cubes using Function Calling Function

def cube(n):
    return n ** 3

def sum_of_cubes(a, b, c):

    return cube(a) + cube(b) + cube(c)

result = sum_of_cubes(4, 6, 5)
print(result)

print()


# Q8 - Strong Number using Factorial Function
# Pending

print()


# Q9 - Palindrome using Reverse Function
# Pending

print()


# Q10 - Even or Odd Digit Sum using sum_digits()
# Pending

print()


# Q11 - Greeting Function using Default Argument

def greetings(name="Guest"):

    print("Hello", name)

greetings()

print()


# Q12 - Area of Rectangle using Default Arguments

def area(length=5, breadth=7):

    print(f"Area of Rectangle = {length * breadth}")

area()

print()


# Q13 - Power Function using Default Exponent
# Pending

print()


# Q14 - Student Details using Keyword Arguments
# Pending

print()


# Q15 - Employee Details using Keyword Arguments
# Pending

print()


# Q16 - Global Variable Example
# Pending

print()


# Q17 - Local Variable Example
# Pending

print()


# Q18 - Local and Global Variable
# Pending

print()


# Q19 - Same Variable Name (Global vs Local)
# Pending

print()


# Q20 - Menu Driven Calculator using Functions
# Pending

print()
