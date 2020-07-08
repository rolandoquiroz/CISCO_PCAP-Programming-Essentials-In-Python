#!/usr/bin/python3
"""
Let's get started on a function to evaluate the Body Mass Index (BMI).
BMI equals weight in kilograms divided by height in meters squared

BMI = (weight in kilograms)/(height in meters)^2

As you can see, the formula gets two values:

    weight (originally in kilograms)
    height (originally in meters)

It seems that this new function will have two parameters.
Its name will be bmi, but if you prefer any other name,
use it instead.

Let's code the function.

The function is complete below (and in the editor window):
"""


def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))

"""
The result produced by the sample invocation looks as follows:

19.283746556473833

The function fulfils our expectations, but it's a bit simple -
it assumes that the values of both parameters are always meaningful.
It's definitely worth checking if they're trustworthy.

Let's check them both and return None if any of them looks suspicious.

"""


def bmi1(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi1(352.5, 1.65))


"""
Look at the code in the editor. There are two things we need to pay
attention to.

First, the test invocation ensures that the protection works properly
- the output is:

None

Second, take a look at the way the backslash ('\') symbol is used. If
you use it in Python code and end a line with it, it will tell Python
to continue the line of code in the next line of code.

It can be particularly useful when you have to deal with long lines of
code and you'd like to improve code readability.

Okay, but there's something we omitted too easily - the imperial measurements.
This function is not too useful for people accustomed to pounds,
feet and inches.

What can be done for them?

We can write two simple functions to convert imperial units to metric ones.
Let's start with pounds.

It is a well-known fact that 1 lb = 0.45359237 kg. We'll use this in our
new function.

This is our helper function, named lbtokg:
"""


def lbtokg(lb):
    return lb * 0.45359237


print(lbtokg(1))

"""
The result of the test invocation looks good:
0.45359237

And now it's time for feet and inches:
1 ft = 0.3048 m, and 1 in = 2.54 cm = 0.0254 m.

The function we've written is named ftintom:
"""


def ftintom(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ftintom(1, 1))


"""
The result of a quick test is:
0.3302

It looks as expected.

Note: we wanted to name the second parameter just in,
not inch, but we couldn't. Do you know why?

in is a Python keyword - it cannot be used as a name.

Let's convert six feet into meters:
"""

print(ftintom(6, 0))

"""
And this is the output:
1.8288000000000002

It's quite possible that sometimes you may want to use
just feet without inches. Will Python help you? Of course it will.

We've modified the code a bit:
"""


def ftintom1(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


print(ftintom1(6))

"""
Now the inch parameter has its default value equal to 0.0.

The code produces the following output - this is what is expected:
1.8288000000000002

Finally, the code is able to answer the question: what is the BMI
of a person 5'7" tall and weighing 176 lbs?

This is the code we have built:
"""

def ftintom2(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lbstokg(lb):
    return lb * 0.45359237


def bmi2(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi2(weight = lbstokg(176), height = ftintom(5, 7)))

"""
And the answer is:
27.565214082533313
"""