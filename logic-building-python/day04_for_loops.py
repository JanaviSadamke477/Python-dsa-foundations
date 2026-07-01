# ================================================================
# Day 4 - For Loop Basics
# Date: 26 June 2026
# ================================================================

# Q1 - Multiplication Table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

print()


# Q2 - Factorial of a Number
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

print()


# Q3 - Factorial from 1 to n
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    print("Factorial of", i, "=", fact)

print()


# Q4 - Prime Numbers from 1 to 100
for n in range(2, 101):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n)

print()


# Q5 - Fibonacci Series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)

    c = a + b
    a = b
    b = c

print()


# Q6 - HCF of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("HCF =", hcf)

print()


# Q7 - Square from 1 to n
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i * i)

print()


# Q8 - Cube from 1 to n
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i * i * i)

print()


# Q9 - Sum of First n Natural Numbers
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)
