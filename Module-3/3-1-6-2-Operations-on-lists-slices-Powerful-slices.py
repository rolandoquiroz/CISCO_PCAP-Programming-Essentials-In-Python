#!/usr/bin/python3
"""
Powerful slices

Fortunately, the solution is at your fingertips - its name is the slice.

A slice is an element of Python syntax that allows you to make a brand new
copy of a list, or parts of a list.

It actually copies the list's contents, not the list's name
"""
# Copyng the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# Copyng part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)
