#!/usr/bin/python3
"""
There once was a hat. The hat contained no rabbit,
but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

    - write a line of code that prompts the user to replace
      the middle number in the list with an integer number
      entered by the user (step 1)
    - write a line of code that removes the last element from
      the list (step 2)
    - write a line of code that prints the length of the
      existing list (step 3.)
"""
# This is an existing list of numbers hidden in the hat.
hatList = [1, 2, 3, 4, 5]

# Step 1: Line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hatList[2] = int(input("Please, gimme an integer: "))
# Step 2: Line of code here that removes the last element from the list.
del (hatList[-1])
# Step 3: Line of code here that prints the length of the existing list.
print("Length of the existing list:", len(hatList))
print(hatList)
