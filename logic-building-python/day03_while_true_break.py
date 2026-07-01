# =================================================================
# Day 3 - While True + Break
# Phase 1: Q1-Q10
# Date: 25 June 2026
# =================================================================

# Q1 - Print Numbers from 1 to 10
i = 1

while True:
    print(i)
    i += 1

    if i > 10:
        break

print()


# Q2 - Take Numbers Until 0 is Entered and Print Their Sum
sum = 0

while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    sum += n

print(f"Sum = {sum}")

print()


# Q3 - Find the Largest Number Until 0 is Entered
largest = None

while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    if largest is None or n > largest:
        largest = n

print(f"Largest Number = {largest}")

print()


# Q4 - Count Positive Numbers Until a Negative Number is Entered
count = 0

while True:
    n = int(input("Enter a number: "))

    if n < 0:
        break

    if n > 0:
        count += 1

print(f"Positive Numbers = {count}")

print()


# Q5 - Sum of Even Digits and Odd Digits Separately
n = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

    n = n // 10

print(f"Sum of Even Digits = {even_sum}")
print(f"Sum of Odd Digits = {odd_sum}")

print()


# Q6 - Menu Driven Calculator
while True:

    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Calculator Closed.")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print(f"Answer = {a + b}")

    elif choice == 2:
        print(f"Answer = {a - b}")

    elif choice == 3:
        print(f"Answer = {a * b}")

    elif choice == 4:
        if b != 0:
            print(f"Answer = {a / b}")
        else:
            print("Division by zero is not possible.")

    else:
        print("Invalid Choice!")

print()


# Q7 - Print Numbers Until 0 is Entered
while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    print(n)

print()


# Q8 - Count Total Numbers Entered Until 0
count = 0

while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    count += 1

print(f"Total Numbers Entered = {count}")

print()


# Q9 - Find the Smallest Number Until 0 is Entered
smallest = None

while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    if smallest is None or n < smallest:
        smallest = n

print(f"Smallest Number = {smallest}")

print()


# Q10 - Count Even and Odd Numbers Until 0 is Entered
even = 0
odd = 0

while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even Numbers = {even}")
print(f"Odd Numbers = {odd}")
