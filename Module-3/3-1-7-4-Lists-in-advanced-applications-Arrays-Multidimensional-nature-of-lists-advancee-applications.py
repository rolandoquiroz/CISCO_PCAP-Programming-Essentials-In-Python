#!/usr/bin/python3
"""
Multidimensional nature of lists: advanced applications

Let's go deeper into the multidimensional nature of lists. To find any
element of a two-dimensional list, you have to use two coordinates:

    a vertical one (row number)
    and a horizontal one (column number).

Imagine that you develop a piece of software for an automatic weather
station. The device records the air temperature on an hourly basis and
does it throughout the month. This gives you a total of 24 × 31 = 744
values. Let's try to design a list capable of storing all these results.

First, you have to decide which data type would be adequate for this
application. In this case, a float would be best, since this thermometer
is able to measure the temperature with an accuracy of 0.1 ℃.

Then you take an arbitrary decision that the rows will record the readings
every hour on the hour (so the row will have 24 elements) and each of the
rows will be assigned to one day of the month (let's assume that each month
has 31 days, so you need 31 rows). Here's the appropriate pair of
comprehensions (h is for hour, d for day):
"""

temps = [[0.0 for h in range(24)] for d in range(31)]

"""
The whole matrix is filled with zeros now. You can assume that it's updated
automatically using special hardware agents. The thing you have to do is to
wait for the matrix to be filled with measurements.

Now it's time to determine the monthly average noon temperature. Add up all
31 readings recorded at noon and divide the sum by 31. You can assume that
the midnight temperature is stored first. Here's the relevant code:
"""

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)
"""

Note: the day variable used by the for loop is not a scalar - each pass through
the temps matrix assigns it with the subsequent rows of the matrix; hence, it's
a list. It has to be indexed with 11 to access the temperature value measured
at noon.

Now find the highest temperature during the whole month - see the code:
"""
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)
"""

Note:

    the day variable iterates through all the rows in the temps matrix;
    the temp variable iterates through all the measurements taken in one day.

Now count the days when the temperature at noon was at least 20 ℃:
"""
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")
