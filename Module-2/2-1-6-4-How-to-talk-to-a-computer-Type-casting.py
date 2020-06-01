#!/usr/bin/python3
"""
- The int() function takes one argument (e.g., a string: int(string))
  and tries to convert it into an integer; if it fails, the whole program
  will fail too (there is a workaround for this situation, but we'll show
  you this a little later);

- The float() function takes one argument (e.g., a string: float(string)
  and tries to convert it into a float (the rest is the same).

"""
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
