#!/usr/bin/python3
"""
As we've said before, omitting both start and end makes a copy of the whole
list

The previously described del instruction is able to delete more than just a
list's element at once - it can delete slices too

Note: in this case, the slice doesn't produce any new list!

Deleting all the elements at once is possible too

del myList[:]
The list becomes empty

Removing the slice from the code changes its meaning dramatically.

Take a look:

del myList

The del instruction will delete the list itself, not its content.
"""
myList = [10, 8, 6, 4, 2]
newList = myList[:]
print(newList)

myList = [10, 8, 6, 4, 2]
del myList[1:3]
print(myList)

myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)

myList = [10, 8, 6, 4, 2]
del myList
# The print() function invocation from the last line of the code
# will then cause a runtime error.
print(myList)
