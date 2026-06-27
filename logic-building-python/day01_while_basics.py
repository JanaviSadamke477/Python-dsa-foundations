# =================================================================
# Day 1 - While Loop Basics
# Phase 1: Q1-Q14, Q21
# Date: 23 June 2026
# ==================================================================

# Q1 - Print 1 to 10
i = 0
while i < 11:   # loops runs from 0 to 10 {alternative: i <= 10}
  print(i)
  i += 1
print()

# Q2 - Print 10 to 1
i = 10
while i > 0:
  print(i)
  i -= 1       # used '-=' because here we are going backwards by 1 position
print()

# Q3 - Print all even numbers 1 to 100
i = 1
while i <= 100:
  if i % 2 == 0:  # if the no. is completely divisible by 2 then it's a even no.
    print(i)
  i += 1 # Moved increment outside the if block{Common mistake if not moved leads to infinite loop}
print()

# Q4 - Print all odd numbers 1 to 100
i = 0
while i <=100:
  if i % 2 != 0:
    print(i)
  i += 1

# Q5 - Multiplication Table of n
n = int(input("Enter the number: "))
i = 1
while i <= 10:
  print(f"{n}*{i} = {n*i}")
  i += 1

# Q5 - Sum of first n natural numbers
i = 1
sum = 0
n = int(input("Enter the number: "))
while i <= n:
    sum += i
    i += 1
print(f"Sum of {n} natural numbers is {sum}")

# Q6 - Sum of all even numbers from 1 to n
i = 1
sum = 0
n = int(input("Enter the number: "))
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(f"Sum of all even no. upto {n} is {sum}")

# Q6 - Sum of all odd numbers from 1 to n
i = 1
sum = 0
n = int(input("Enter the number: "))
while i <= n:
    if i % 2 != 0:
        sum += i
    i += 1
print(f"Sum of all odd no. upto {n} is {sum}")

# Q7 - Product of all digits of a number
num_str = '1234567'           # The number as a string
product = 1                   # Initialize product to 1 (multiplying by 0 would make everything 0)
i = 0                         # Initialize index for iteration
while i < len(num_str):
  digit = int(num_str[i])     # Get the digit at the current index and convert it to an integer
  product *= digit            # Multiply the current product by the digit
  i += 1                      # Move to the next digit
print(f"The product of the digits in {num_str} is: {product}")

# Q8 - Count total digits in a number
n = 12345678
print(len(str(n)))

# Q9 -  Reverse a number
n = str(1234567)
reversed_n = ""
i = len(n) - 1
while i >= 0:
  reversed_n = reversed_n + n[i]
  i -= 1
print(reversed_n)

# Q10 - Check Palindrome
og = "radar"
reverse_og=""
i = len(og)-1
while i >= 0:
  reverse_og = reverse_og + og[i]
  i -= 1
print(reverse_og)
if og == reverse_og:
  print("Palindrome")
else:
  print("Not Palindrome")

# Q11 - Sum of digits of a number
n = 1234
sum = 0
while n > 0:
  digit = n % 10
  sum += digit
  n = n // 10
print(f"Sum is {sum}")

# Q12 - Square of a number
n = int(input("Enter the number: "))
i = 0
while i <= n:
  print(f"{n}**{i} = {n**i}")
  i += 1

# Q13 - Square from 1 to n
n = int(input("Enter a number: "))
i = 1
while i <= n:
  square = i * i
  print(f"The square of {i} is {square}")
  i += 1

