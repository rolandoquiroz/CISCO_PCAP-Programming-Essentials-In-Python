#!/usr/bin/python3
"""
Replication

The * (asterisk) sign, when applied to a string
and number (or a number and string, as it remains
commutative in this position) becomes a replication operator:

string * number
number * string

It replicates the string the same number of times
specified by the number.
"""
print('James' * 3)
print(3 * 'an')
print(5 * '2')

'''
This simple program "draws" a rectangle,
making use of an old operator (+) in a new role:
'''
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
