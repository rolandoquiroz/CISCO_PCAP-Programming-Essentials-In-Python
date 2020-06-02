#!/usr/bin/python3
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here

print(str((hour + (mins + dura) // 60) % 24) + ':' + str((mins + dura) % 60))
