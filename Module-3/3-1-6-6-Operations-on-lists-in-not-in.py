#!/usr/bin/python3
"""
The in and not in operators

Python offers two very powerful operators, able to look through the list in
order to check whether a specific value is stored inside the list or not.

These operators are:

elem in myList
elem not in myList

The first of them (in) checks if a given element (its left argument) is
currently stored somewhere inside the list (the right argument) - the operator
returns True in this case.

The second (not in) checks if a given element (its left argument) is absent in
a list - the operator returns True in this case.

Look at the code in the editor. The snippet shows both operators in action.
Can you guess its output? Run the program to check if you were right.
"""
myList = [0, 3, 12, 8, 2]

print(5 in myList)
print(5 not in myList)
print(12 in myList)
