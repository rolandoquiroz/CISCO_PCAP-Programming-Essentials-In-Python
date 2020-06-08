#!/usr/bin/python3
"""
The length of a list may vary during execution.
New elements may be added to the list, while others
may be removed from it. This means that the list is a very dynamic entity.

If you want to check the list's current length, you can use a function
named len() (its name comes from length).

The function takes the list's name as an argument, and returns the number
of elements currently stored inside the list (in other words - the list's
length).
"""
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # printing original list content

numbers[0] = 111
print("\nPrevious list content:", numbers)  # printing previous list content

numbers[1] = numbers[4]  # copying value of the fifth element to the second
print("Previous list content:", numbers)  # printing previous list content

print("\nList length:", len(numbers))  # printing the list's length
