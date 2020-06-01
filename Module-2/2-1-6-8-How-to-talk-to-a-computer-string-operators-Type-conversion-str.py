#!/usr/bin/python3
"""
You can also convert a number into a string,
which is way easier and safer - this operation is always possible.

A function capable of doing that is called str():

str(number)
"""
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** 0.5))
