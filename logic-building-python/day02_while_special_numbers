# =================================================================
# Day 2 - While Loop Intermediate
# Phase 1: Q1-Q8
# Date: 24 June 2026
# =================================================================

# Q1 - Factorial of a Number
n = int(input("Enter a number: "))
i = 1
fac = 1

while i <= n:
    fac *= i
    i += 1

print(f"Factorial of {n} is {fac}")
print()

# Q2 - Armstrong Number Check
n = int(input("Enter a number: "))
str_n = str(n)
count = len(str_n)
i = 0
sum = 0

while i < count:
    digit = int(str_n[i])
    sum += digit ** count
    i += 1

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
print()

# Q3 - Perfect Number Check
n = int(input("Enter a number: "))
i = 1
sum = 0

while i < n:
    if n % i == 0:
        sum += i
    i += 1

if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
print()

# Q4 - Prime Number Check
n = int(input("Enter a number: "))
count = 0
i = 1

while i <= n:
    if n % i == 0:
        count += 1
    i += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
print()

# Q5 - Fibonacci Series up to n Terms
a = 0
b = 1

n = int(input("Enter number of terms: "))
i = 1

while i <= n:
    print(a)
    next_val = a + b
    a = b
    b = next_val
    i += 1

print()

# Q6 - All Factors of a Number
n = int(input("Enter a number: "))
i = 1

print(f"Factors of {n} are:")

while i <= n:
    if n % i == 0:
        print(i)
    i += 1

print()

# Q7 - HCF of Two Numbers (Euclidean Algorithm)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    temp = a % b
    a = b
    b = temp

print(f"HCF is {a}")
print()

# Q8 - LCM of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while y != 0:
    temp = x % y
    x = y
    y = temp

hcf = x
lcm = (a * b) // hcf

print(f"LCM is {lcm}")
