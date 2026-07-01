# =================================================================
# Day 7 - Advanced Series & Number Programs
# Date: 29 June 2026
# =================================================================

# Q1 - x - x²/2! + x³/3! - x⁴/4! + ... + xⁿ/n!
x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(1, n + 1):

    fact = 1

    for j in range(1, i + 1):
        fact *= j

    term = (x ** i) / fact

    if i % 2 == 0:
        sum -= term
    else:
        sum += term

print(f"Sum = {sum}")

print()


# Q2 - Strong Number Check
n = int(input("Enter a number: "))

original = n
sum = 0

while n > 0:

    digit = n % 10

    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    sum += fact

    n //= 10

if sum == original:
    print("Strong Number")
else:
    print("Not Strong Number")

print()


# Q3 - First Number (1-100) Whose Digit Sum is Even
for i in range(1, 101):

    temp = i
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10

    if sum % 2 == 0:
        print(i)
        break

print()


# Q4 - Count Numbers (1-500) Divisible by 7 but not by 5
count = 0

for i in range(1, 501):

    if i % 7 == 0 and i % 5 != 0:
        count += 1

print(f"Count = {count}")

print()


# Q5 - All Palindrome Numbers from 1 to 500
for i in range(1, 501):

    temp = i
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if i == reverse:
        print(i)

print()


# Q6 - Numbers (1-100) Whose Digit Sum is Multiple of 3
for i in range(1, 101):

    temp = i
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10

    if sum % 3 == 0:
        print(i)

print()


# Q7 - Numbers Whose Binary Representation has Even Count of 1's
for i in range(1, 101):

    temp = i
    count = 0

    while temp > 0:

        bit = temp % 2

        if bit == 1:
            count += 1

        temp //= 2

    if count % 2 == 0:
        print(i)

print()


# Q8 - Sum of Even Digits and Odd Digits Separately
n = int(input("Enter a number: "))

sum_even = 0
sum_odd = 0

while n > 0:

    digit = n % 10

    if digit % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit

    n //= 10

print(f"Sum of Even Digits = {sum_even}")
print(f"Sum of Odd Digits = {sum_odd}")

print()


# Q9 - All Armstrong Numbers from 1 to 1000
for n in range(1, 1001):

    str_n = str(n)
    count = len(str_n)

    sum = 0

    for char in str_n:
        digit = int(char)
        sum += digit ** count

    if sum == n:
        print(n)

print()


# Q10 - All Perfect Numbers from 1 to 1000
for n in range(1, 1001):

    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum += i

    if sum == n:
        print(n)

print()


# Q11 - Number (1-n) Having Maximum Digit Sum
n = int(input("Enter a number: "))

max_sum = 0
max_number = 0

for i in range(1, n + 1):

    temp = i
    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10

    if digit_sum > max_sum:
        max_sum = digit_sum
        max_number = i

print(f"Number = {max_number}")
print(f"Maximum Digit Sum = {max_sum}")

print()


# Q12 - Print i × i Pattern (Number Triangle Variant)
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    for j in range(i):
        print(i, end=" ")

    print()

print()


# Q13 - Numbers Between a and b Divisible by 7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):

    if i % 7 == 0:
        print(i)
