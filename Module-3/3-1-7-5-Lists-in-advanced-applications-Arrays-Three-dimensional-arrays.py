#!/usr/bin/python3
"""
Three-dimensional arrays

Python does not limit the depth of list-in-list inclusion. Here you can see
an example of a three-dimensional array:

Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors
each. There are 20 rooms on each floor. For this, you need an array which
can collect and process information on the occupied/free rooms.

First step - the type of the array's elements. In this case, a Boolean value
(True/False) would fit.

Step two - calm analysis of the situation. Summarize the available
information: three buildings, 15 floors, 20 rooms.

Now you can create the array:
"""

rooms = [[[False for r in range(20)] for f in range(15)] for b in range(3)]

"""
The first index (0 through 2) selects one of the buildings; the second
(0 through 14) selects the floor, the third (0 through 19) selects the room
number. All rooms are initially free.

Now you can book a room for two newlyweds: in the second building, on the
tenth floor, room 14:
"""

rooms[1][9][13] = True

"""
and release the second room on the fifth floor located in the first
building:
"""

rooms[0][4][1] = False

"""
Check if there are any vacancies on the 15th floor of the third building:
"""

vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1

"""
The vacancy variable contains 0 if all the rooms are occupied, or the number
of available rooms otherwise.
"""