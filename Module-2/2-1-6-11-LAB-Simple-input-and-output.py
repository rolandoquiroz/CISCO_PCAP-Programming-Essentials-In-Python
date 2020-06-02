#!/usr/bin/python3
"""
Your task is to prepare a simple code able to evaluate the end time of
a period of time, given as a number of minutes (it could be arbitrarily
large). The start time is given as a pair of hours (0..23) and minutes
(0..59). The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes,
it will end at 13:16.

Test Data

Sample input:
12
17
59

Expected output: 13:16

Sample input:
23
58
642

Expected output: 10:40

Sample input:
0
1
2939

Expected output: 1:0
"""
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here

print(str((hour + (mins + dura) // 60) % 24) + ':' + str((mins + dura) % 60))
