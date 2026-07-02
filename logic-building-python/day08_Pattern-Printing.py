# =================================================================
# Day 7 - Pattern Printing (Nested Loops)
# Date: 29 June 2026
# =================================================================

# Q1 - Square Pattern (n x n Stars)
n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print()


# Q2 - Increasing Triangle (*, **, *** ...)
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print()


# Q3 - Right Aligned Triangle
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    for space in range(n - i):
        print(" ", end=" ")

    for star in range(i):
        print("*", end=" ")

    print()

print()


# Q4 - Centered Pyramid
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    for space in range(n - i):
        print(" ", end=" ")

    for star in range(2 * i - 1):
        print("*", end=" ")

    print()

print()


# Q5 - Number Sequence Rows
# 1
# 12
# 123
# 1234

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end="")

    print()

print()


# Q6 - Consecutive Numbers Row-wise
# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = int(input("Enter number of rows: "))

num = 1

for i in range(1, n + 1):

    for j in range(i):
        print(num, end=" ")
        num += 1

    print()

print()


# Q7 - Alphabet Triangle
# A
# B C
# D E F
# G H I J

n = int(input("Enter number of rows: "))

ch = 65

for i in range(1, n + 1):

    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1

    print()

print()


# Q8 - Alphabet Increasing Rows
# A
# AB
# ABC
# ABCD

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    ch = 65

    for j in range(i):
        print(chr(ch), end="")
        ch += 1

    print()

print()


# Q9 - Palindrome Number Pattern
# 1
# 121
# 12321
# 1234321

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

print()


# Q10 - Diamond Pattern

n = int(input("Enter number of rows: "))

# Upper Half
for i in range(1, n + 1):

    for space in range(n - i):
        print(" ", end=" ")

    for star in range(2 * i - 1):
        print("*", end=" ")

    print()

# Lower Half
for i in range(n - 1, 0, -1):

    for space in range(n - i):
        print(" ", end=" ")

    for star in range(2 * i - 1):
        print("*", end=" ")

    print()
