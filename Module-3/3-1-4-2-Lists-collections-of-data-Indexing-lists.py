#!/usr/bin/python3
"""
Indexing lists

How do you change the value of a chosen element in the list?
Let's assign a new value of 111 to the first element in the list.
We do it this way:
"""
numbers = [10, 5, 7, 2, 1]
print("Original list content: ", numbers)

numbers[0] = 111
print("New list content: ", numbers)

"""
And now we want the value of the fifth element to be copied to the
second element - can you guess how to do it?
"""
numbers[1] = numbers[4]
print("New list content: ", numbers)
