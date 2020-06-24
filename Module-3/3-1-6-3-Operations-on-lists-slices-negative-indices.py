#!/usr/bin/python3
"""
Slices - negative indices

Look at the snippet below:

myList[start:end]

To repeat:

    start is the index of the first element included in the slice;
    end is the index of the first element not included in the slice.

If the start specifies an element lying further than the one described
by the end (from the list's beginning point of view), the slice will
be empty.

If you omit the start in your slice, it is assumed that you want to get
a slice beginning at the element with index 0.

In other words, the slice of this form:
myList[:end]

is a more compact equivalent of:
myList[0:end]

Similarly, if you omit the end in your slice, it is assumed that you want
the slice to end at the element with the index len(myList).

In other words, the slice of this form:
myList[start:]

is a more compact equivalent of:
myList[start:len(myList)]
"""
myList = [10, 8, 6, 4, 2]
newList = myList[1:-1]
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[-1:1]
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[:3]
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[3:]
print(newList)
