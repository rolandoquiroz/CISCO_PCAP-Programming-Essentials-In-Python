#!/usr/bin/python3
"""
Positional parameter passing

A technique which assigns the ith (first, second, and so on) argument to the
ith (first, second, and so on) function parameter is called positional
parameter passing, while arguments passed in this way are named positional
arguments.

You've used it already, but Python can offer a lot more. We're going to tell
you about it now.
"""


def myFunction(a, b, c):
    print(a, b, c)


myFunction(1, 2, 3)

"""
Note: positional parameter passing is intuitively used by people in many social
occasions. For example, it may be generally accepted that when we introduce
ourselves we mention our first name(s) before our last name, e.g.,
"My name's John Doe."

Incidentally, Hungarians do it in reverse order.

Let's implement that social custom in Python. The following function will be
responsible for introducing somebody:
"""


def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)


introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

"""

Can you guess the output? Run the code and find out if you were right.

Now imagine that the same function is being used in Hungary. In this case,
the code would look like this:
"""


def introduction1(firstName, lastName):
    print("Hello, my name is", firstName, lastName)


introduction1("Skywalker", "Luke")
introduction1("Quick", "Jesse")
introduction1("Kent", "Clark")
"""
The output will look different. Can you guess it?

Run the code to see if you were right here, too. Are you surprised?

Can you make the function more culture-independent
"""
