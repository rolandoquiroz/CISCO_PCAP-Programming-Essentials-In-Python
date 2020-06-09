#!/usr/bin/python3
"""
Adding elements to a list: continued

You can start a list's life by making it empty
(this is done with an empty pair of square brackets or
using the list() constructor)
and then adding new elements to it as needed.

"""
myList = []  # Method 1: empty list: empty pair of square brackets

for i in range(5):
    myList.append(i + 1)
print(myList)

myList = list()  # Method 2: empty list: list() constructor

for i in range(5):
    myList.insert(0, 5 - i)
print(myList)

"""
Get the same sequence, but in reverse order
(this is the merit of using the insert() method).
"""
otherList = []  # Method 1: empty list: empty pair of square brackets

for i in range(5):
    otherList.append(5 - i)
print(otherList)

otherList = list()  # Method 2: empty list: list() constructor

for i in range(5):
    otherList.insert(0, i + 1)
print(otherList)
