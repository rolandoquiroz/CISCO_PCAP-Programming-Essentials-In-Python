#!/usr/bin/python3
"""
Our next example refers to the earlier program to find
the length of a hypotenuse. Let's rewrite it and make
it able to read the lengths of the legs from the console.
"""
leg_a = float(input('Input first leg lenght: '))
leg_b = float(input('Input second leg lenght: '))
print('Hypotenuse lenght is', (leg_a ** 2 + leg_b ** 2) ** 0.5)
