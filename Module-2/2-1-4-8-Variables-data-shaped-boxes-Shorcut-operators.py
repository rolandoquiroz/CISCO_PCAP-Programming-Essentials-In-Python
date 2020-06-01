#!/usr/bin/python3
"""
If op is a two-argument operator (this is a very important condition)
and the operator is used in the following context:
variable = variable op expression

It can be simplified and shown as follows:
variable op= expression
"""
x = 4
x = x * 2
x *= 2
print(x)

sheep = 664
sheep = sheep + 1
sheep += 1
print(sheep)

i = 8
j = 6
i = i + 2 * j
i += 2j
print(i)

var = 12
var = var / 2
var /= 2
print(var)

rem = 5
rem = rem % 10
rem %= 10
print(rem)

j = j - (i + var + rem)
j -= (i + var + rem)
print(j)

x = x ** 2
x **= 2
print(x)
