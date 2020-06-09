#!/usr/bin/python3
"""
Now you can easily swap the list's elements to reverse their order:
"""
myList = [10, 1, 8, 3, 5]
print(myList)

for i in range(len(myList) // 2):
    myList[i], myList[len(myList)-1-i] = myList[len(myList)-1-i], myList[i]

print(myList)
