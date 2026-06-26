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
  if i % 2 == 0:  # if the no. is completely divisible by 2 then it's a prime no.
    print(i)
  i += 1 # Moved increment outside the if block{Common mistake if not moved leads to infinite loop}
print()

# Q4 - Print all odd numbers 1 to 100
i = 0
while i <=100:
  if i % 2 != 0:
    print(i)
  i += 1
