#!/usr/bin/python3
"""
It's legal, and possible, to have a variable named the same as a function's
parameter.

The snippet illustrates the phenomenon:

def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)

A situation like this activates a mechanism called shadowing:

    parameter x shadows any variable of the same name, but...
    ... only inside the function defining the parameter.

The parameter named number is a completely different entity from the variable
named number.

This means that the snippet above will produce the following output:
Enter a number: 1
1234
"""


def message(number):
    print("Enter a number:", number)


message(4)

number = 1234
message(1)
print(number)

"""
A function can have as many parameters as you want, but the more parameters
you have, the harder it is to memorize their roles and purposes.
Functions as a black box concept

Let's modify the function - it has two parameters now:
def message(what, number):
    print("Enter", what, "number", number)

This also means that invoking the function will require two arguments.

The first new parameter is intended to carry the name of the desired value.

Here it is:
"""


def message1(what, number):
    print("Enter", what, "number", number)


message1("telephone", 11)
message1("price", 6)
message1("number", "number")
