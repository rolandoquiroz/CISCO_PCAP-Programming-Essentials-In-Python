#!/usr/bin/python3
"""
Parametrized functions - more details

It happens at times that a particular parameter's values are in use more
often than others. Such arguments may have their default (predefined)
values taken into consideration when their corresponding arguments have
been omitted.

They say that the most popular English last name is Smith. Let's try to
take this into account.

The default parameter's value is set using clear and pictorial syntax:
"""


def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)


"""
You only have to extend the parameter's name with the = sign, followed
by the default value.

Let's invoke the function as usual:
"""

introduction("James", "Doe")

"""
Can you guess the output of the program? Run it and check if you were
right.

And? Everything looks the same, but when you invoke the function in a
way that looks a bit suspicious at first sight, like this:
"""

introduction("Henry")

# or this:

introduction(firstName="William")

"""
there will be no error, and both invocations will succeed, while the
console will show the following output:

Hello, my name is Henry Smith
Hello, my name is William Smith

Test it.

You can go further if it's useful. Both parameters have their default
values now, look at the code below:
"""


def introduction1(firstName="John", lastName="Smith"):
    print("Hello, my name is", firstName, lastName)


"""
This makes the following invocation absolutely valid:
"""

introduction1()

"""
And this is the expected output:
Hello, my name is John Smith

If you use one keyword argument, the remaining one will take the default
value:
"""

introduction1(lastName="Hopkins")

"""
The output is:
Hello, my name is John Hopkins

Test it.

Congratulations - you have just learned the basic ways of communicating
with functions.
"""
