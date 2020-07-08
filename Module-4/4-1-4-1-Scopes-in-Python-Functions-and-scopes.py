#!/usr/bin/python3
"""
Functions and scopes

Let's start with a definition:

The scope of a name (e.g., a variable name) is the part of a code where the
name is properly recognizable.

For example, the scope of a function's parameter is the function itself.
The parameter is inaccessible outside the function.

Let's check it. Look at the code in the editor. What will happen when
you run it?
"""


def scopeTest():
    x = 123


scopeTest()
print(x)

"""
The program will fail when run. The error message will read:
NameError: name 'x' is not defined

Let's start by checking whether or not a variable created
outside any function is visible inside the functions. In other
words, does a variable's name propagate into a function's body?

Look at the code in the editor. Our guinea pig is there.
"""


def myFunction():
    print("Do I know that variable?", var)


var = 1
myFunction()
print(var)
