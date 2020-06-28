#!/usr/bin/python3
"""
Your task is to write and test a function which takes two arguments
(a year and a month) and returns the number of days for the given
month/year pair (while only February is sensitive to the year value,
your function should be universal).

The initial part of the function is ready. Now, convince the function
to return None if its arguments don't make sense.

Of course, you can (and should) use the previously written and tested
function (LAB 4.1.3.6). It may be very helpful. We encourage you to
use a list filled with the months' lengths. You can create it inside
the function - this trick will significantly shorten the code.

We've prepared a testing code. Expand it to include more test cases
"""


def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(year, month):
    feb = 28
    if isYearLeap(year):
        feb = 29
    months = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month-1]


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
