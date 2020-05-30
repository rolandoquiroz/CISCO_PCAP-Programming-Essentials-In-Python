#!/usr/bin/python3
"""
When you want to use any numbers that are very large
or very small, you can use scientific notation.
Take, for example, the speed of light, expressed in
meters per second. Written directly it would look
like this: 300000000.
To avoid writing out so many zeros, physics textbooks
use an abbreviated form, which you have probably already
seen: 3 x 10^8.

It reads: three times ten to the power of eight.

In Python, the same effect is achieved in a slightly
different way - take a look:

3E8
3e8

The letter E (you can also use the lower-case letter e -
it comes from the word exponent) is a concise record of
the phrase times ten to the power of.

Note:

    the exponent (the value after the E) has to be an integer;
    the base (the value in front of the E) may be an integer.
"""
print(3E8)
print(3e8)

"""
A physical constant called Planck's constant (and denoted as h),
according to the textbooks, has the value of: 6.62607 x 10-34.
"""
print(6.62607E-34)

"""
For example, let's say you've decided to use the following
float literal:
0.0000000000000000000001

When you run this literal through Python:
print(0.0000000000000000000001)

this is the result:
1e-22

Python always chooses the more economical form of the number's
presentation, and you should take this into consideration when
creating literals.
"""
print(0.0000000000000000000001)
