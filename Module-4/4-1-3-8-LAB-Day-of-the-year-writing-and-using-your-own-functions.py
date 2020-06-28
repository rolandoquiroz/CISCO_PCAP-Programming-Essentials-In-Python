#!/usr/bin/python3
"""
Your task is to write and test a function which takes three arguments (a
year, a month, and a day of the month) and returns the corresponding day
of the year, or returns None if any of the arguments is invalid.

Use the previously written and tested functions. Add some test cases to
the code. This test is only a beginning.
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


def dayOfYear(year, month, day):
    days = 0
    for m in range(1, month):
        days += daysInMonth(year, m)
    return (days + day)


print(dayOfYear(2000, 12, 31))
