#!/usr/bin/python3
"""
Effects and results: lists and functions

There are two additional questions that should be answered here.

The first is: may a list be sent to a function as an argument?

Of course it may! Any entity recognizable by Python can play the

role of a function argument, although it has to be assured that
the function is able to cope with it.

So, if you pass a list to a function, the function has to handle
it like a list.

A function like this one here:
"""


def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

# and invoked like this:


print(list_sum([5, 4, 3]))


"""
will return 12 as a result, but you should expect problems if
you invoke it in this risky way:
"""

# print(list_sum(5))

""""
Python's response will be unequivocal:

TypeError: 'int' object is not iterable

This is caused by the fact that a single integer value mustn't
be iterated through by the for loop.

The second question is: may a list be a function result?

Yes, of course! Any entity recognizable by Python can be a function result.
"""


def strangeListFunction(n):
    strangeList = []

    for i in range(0, n):
        strangeList.insert(0, i)

    return strangeList


print(strangeListFunction(5))


"""
The program's output will be like this:
[4, 3, 2, 1, 0]

Now you can write functions with and without results.

Let's dive a little deeper into the issues connected with variables in
functions.

This is essential for creating effective and safe functions.
"""
