# =================================================================
# Week 2 - Day 1 : Functions Basics
# Date: 05 July 2026
# =================================================================

# Q1 - Function to print "Good Morning"

def greetings():
    print("Good Morning")

greetings()

print()


# Q2 - Function to print Hello + Name

def greetings(name):
    print("Hello", name)

greetings("Janavi")

print()


# Q3 - Function to print sum of two numbers

def add(a, b):
    print(a + b)

add(10, 20)

print()


# Q4 - Function to check Even or Odd

def check(n):
    if n % 2 == 0:
        print(f"{n} is Even.")
    else:
        print(f"{n} is Odd.")

check(4)
check(7)

print()


# Q5 - Function to print the larger of two numbers

def larger(a, b):

    if a > b:
        print(f"{a} is larger than {b}.")

    elif b > a:
        print(f"{b} is larger than {a}.")

    else:
        print("Both numbers are equal.")

larger(34, 66)
larger(90, 32)
larger(50, 50)

print()


# Q6 - Function to return square of a number

def square(n):
    return n * n

result = square(4)
print(result)

result = square(13)
print(result)

print()


# Q7 - Function to return cube of a number

def cube(n):
    return n ** 3

result = cube(4)
print(result)

result = cube(13)
print(result)

print()


# Q8 - Function to return sum of two numbers

def add(a, b):
    return a + b

result = add(20, 30)
print(result)

print()


# Q9 - Function to return product of two numbers

def product(a, b):
    return a * b

result = product(10, 5)
print(result)

print()


# Q10 - Function to return Even or Odd

def even_odd(n):

    if n % 2 == 0:
        return "Even"

    else:
        return "Odd"

result = even_odd(17)
print(result)

print()


# Q11 - Function to check Prime Number

def is_prime(n):

    if n <= 1:
        print(f"{n} is not a Prime Number.")
        return

    count = 0

    for i in range(2, n):

        if n % i == 0:
            count += 1

    if count == 0:
        print(f"{n} is a Prime Number.")

    else:
        print(f"{n} is not a Prime Number.")

is_prime(23)
is_prime(18)
is_prime(1)

print()


# Q12 - Function to return Factorial

def factorial(n):

    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

result = factorial(7)
print(result)

print()


# Q13 - Function to return Sum of Digits

def sum_digits(n):

    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    return total

result = sum_digits(12345)
print(result)

print()


# Q14 - Function to return Reverse of a Number

def reverse_number(n):

    reverse = 0

    while n > 0:

        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return reverse

result = reverse_number(12345)
print(result)

print()


# Q15 - Function to check Palindrome Number

def palindrome(n):

    original = n
    reverse = 0

    while n > 0:

        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    if original == reverse:
        return "Palindrome"

    else:
        return "Not Palindrome"

result = palindrome(121)
print(result)

result = palindrome(123)
print(result)

print()


# Q16 - Function to calculate Area of Rectangle

def rectangle(length, breadth):
    return length * breadth

print(rectangle(10, 5))

print()


# Q17 - Function to calculate Area of Circle

def circle(radius):

    pi = 3.14

    return pi * radius * radius

print(circle(7))

print()


# Q18 - Function to calculate Simple Interest

def simple_interest(p, r, t):

    return (p * r * t) / 100

print(simple_interest(10000, 10, 2))

print()


# Q19 - Function to return Greatest of Three Numbers

def greatest(a, b, c):

    if a > b and a > c:
        return a

    elif b > a and b > c:
        return b

    elif c > a and c > b:
        return c

    else:
        return "All numbers are equal."

print(greatest(34, 87, 65))
print(greatest(12, 12, 12))

print()


# Q20 - Function to count Digits in a Number

def count_digits(n):

    count = 0

    while n > 0:

        count += 1
        n //= 10

    return count

print(count_digits(123456789))

print()
