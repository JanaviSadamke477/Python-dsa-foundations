# =================================================================
# Week 2 - Day 2 : Intermediate Functions
# Phase 1 : Q1 - Q20
# Date : 08 July 2026
# =================================================================


# Q1 - Return Maximum of Two Numbers

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(10, 12))
print()


# Q2 - Return Minimum of Two Numbers

def minimum(a, b):
    if a < b:
        return a
    else:
        return b

print(minimum(10, 12))
print()


# Q3 - Return Absolute Difference

def difference(a, b):
    return abs(a - b)

print(difference(56, 12))
print()


# Q4 - Return Average of Three Numbers

def average(a, b, c):
    return (a + b + c) / 3

print(average(34, 65, 78))
print()


# Q5 - Return Sum of First n Natural Numbers

def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

print(sum_n(10))
print()


# Q6 - Sum of Squares using Function Calling Function

def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(4, 6))
print()


# Q7 - Sum of Cubes using Function Calling Function

def cube(n):
    return n ** 3

def sum_of_cubes(a, b, c):
    return cube(a) + cube(b) + cube(c)

print(sum_of_cubes(4, 6, 5))
print()


# Q8 - Strong Number using Factorial Function

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


def strong_number(n):

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    if total == n:
        return "Strong Number"
    else:
        return "Not a Strong Number"

print(strong_number(145))
print()


# Q9 - Palindrome using Reverse Function

def palindrome(n):

    temp = n
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if reverse == n:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(palindrome(121))
print()


# Q10 - Sum of Digits Even or Odd

def sum_digits(n):

    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    if total % 2 == 0:
        return "Even Digit Sum"
    else:
        return "Odd Digit Sum"

print(sum_digits(12653))
print()


# Q11 - Greeting Function using Default Argument

def greetings(name="Guest"):
    print("Hello", name)

greetings()
greetings("Janavi")
print()


# Q12 - Area using Default Arguments

def area(length=5, breadth=7):
    return length * breadth

print(area())
print(area(10, 8))
print()


# Q13 - Power Function using Default Exponent

def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))
print()


# Q14 - Student Details using Keyword Arguments

def student(name, age):
    print("Name :", name)
    print("Age  :", age)

student(name="Janavi", age=21)
print()


# Q15 - Employee Details using Keyword Arguments

def employee(name, salary):
    print("Employee :", name)
    print("Salary   :", salary)

employee(name="Rahul", salary=50000)
print()


# Q16 - Global Variable

college = "ABC College"

def display():
    print(college)

display()
print()


# Q17 - Local Variable

def show():
    name = "Janavi"
    print(name)

show()

# print(name)   # Uncomment to see NameError

print()


# Q18 - Local + Global Variables

college = "PCCOE"

def details():
    name = "Janavi"

    print(name)
    print(college)

details()
print()


# Q19 - Same Variable Name (Local vs Global)

count = 100

def test():

    count = 10

    print("Local Count :", count)

test()

print("Global Count:", count)

print()


# Q20 - Menu Driven Calculator using Functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:

    print("\n===== Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Calculator Closed.")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Answer =", add(a, b))

    elif choice == 2:
        print("Answer =", subtract(a, b))

    elif choice == 3:
        print("Answer =", multiply(a, b))

    elif choice == 4:
        print("Answer =", divide(a, b))

    else:
        print("Invalid Choice")
