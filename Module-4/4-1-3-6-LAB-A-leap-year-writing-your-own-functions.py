#!/usr/bin/python3
"""
Your task is to write and test a function which takes one argument (a year)
and returns True if the year is a leap year, or False otherwise.

The seed of the function is already sown in the skeleton code in the editor.

Note: we've also prepared a short testing code, which you can use to test
your function.

The code uses two lists - one with the test data, and the other containing
the expected results. The code will tell you if any of your results are
invalid.
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


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
