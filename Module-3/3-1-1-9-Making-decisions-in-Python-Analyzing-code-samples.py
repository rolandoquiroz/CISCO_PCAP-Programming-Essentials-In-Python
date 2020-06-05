#!/usr/bin/python3
"""
Example 1: How to identify the larger of two numbers:
"""
# read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# print the result
print("The larger number is:", larger_number)


"""
Example 3: Let's find the largest of three numbers.
Will it enlarge the code? A bit.

We assume that the first value is the largest.
Then we verify this hypothesis with the two remaining values.

Look at the code below:
"""
# read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# we check if the second number is larger than current largest_number
# and update largest_number if needed
if number2 > largest_number:
    largest_number = number2

# we check if the third number is larger than current largest_number
# and update largest_number if needed
if number3 > largest_number:
    largest_number = number3

# print the result
print("The largest number is:", largest_number)
