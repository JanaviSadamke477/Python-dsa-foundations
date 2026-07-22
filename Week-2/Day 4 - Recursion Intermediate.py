'''
def product_digits(n):
    if n == 0:
        return 1
        
    digit = n % 10
    return digit * product_digits(n//10)
print(product_digits(12345))
'''
'''
def largest_digit(n):
    if n < 10:
        return n
        
    digit = n % 10
    return max(digit, largest_digit(n//10))
print(largest_digit(5848))
'''
'''
def smallest_digit(n):
    if n < 10:
        return n
        
    digit = n % 10
    return min(digit, smallest_digit(n//10))
print(smallest_digit(5848))
'''
'''
def reverse_number(n, rev):
    if n == 0:
        return rev
        
    digit = n % 10
    rev = rev * 10 + digit
    return reverse_number(n//10, rev)
print(reverse_number(4562, 0))
'''

'''
def reverse_number(n, rev):
    if n == 0:
        return rev
        
    digit = n % 10
    rev = rev * 10 + digit
    return reverse_number(n//10, rev)

def is_palindrome(n):
    rev = reverse_number(n, 0)
    
    if rev == n:
        return "Palindrome"
    else:
        return " Not Palindrome"
print(is_palindrome(4562))
'''
'''
def count_zeros(n):
    if n == 0:
        return 0
        
    digit = n % 10
    if digit == 0:
        return 1 + count_zeros(n//10)
    else:
        return count_zeros(n//10)
print(count_zeros(10508050))
'''

'''
def sum_squares(n):
    if n == 1:
        return 1

    return n*n + sum_squares(n - 1)
print(sum_squares(5))
'''
'''
def sum_cubes(n):
    if n == 1:
        return 1

    return n*n*n + sum_cubes(n - 1)
print(sum_cubes(6))
'''

'''
def print_digits_left_to_right(n):
    if n == 0:
        return 
    
    digit = n % 10
    return print_digits_left_to_right(n//10)
    print(digit)
print(print_digits_left_to_right(5348))
'''

'''
def print_digits_left_to_right(n):
    if n == 0:
        return

    print_digits_left_to_right(n // 10)

    digit = n % 10
    print(digit)

print_digits_left_to_right(5348)
'''
'''
def decimal_to_binary(n):
    if n == 0:
        return

    decimal_to_binary(n//2)

    print(n % 2, end="")
decimal_to_binary(13)
'''



