#!/usr/bin/python3
"""
What is the result of the following comparison?

2 == 2.

This question is not as easy as the first one.
Luckily, Python is able to convert the integer
value into its real equivalent, and consequently
the answer is True.

Priority 	Operator
1 	+, - 	unary
2 	**
3 	*, /, //, %
4 	+, - 	binary
5 	<, <=, >, >=
6 	==, !=

Write a simple two-line program that takes the parameter n as input,
which is an integer, and prints False if n is less than 100,
and True if n is greater than or equal to 100.

Don't create any if blocks (we're going to talk about them very soon).
Test your code using the data we've provided for you.

Test Data

Sample input: 55

Expected output: False

Sample input: 99

Expected output: False

Sample input: 100

Expected output: True

Sample input: 101

Expected output: True

Sample input: -5

Expected output: False

Sample input: +123

Expected output: True
"""
n = int(input("Please give me a number: "))
print(n >= 100)
