#!/usr/bin/python3
"""
The Beatles were one of the most popular music group of the 1960s,
and the best-selling band in history. Some people consider them
to be the most influential act of the rock era. Indeed, they were
included in Time magazine's compilation of the 20th Century's 100
most influential people.

The band underwent many line-up changes, culminating in 1962 with
the line-up of John Lennon, Paul McCartney, George Harrison, and
Richard Starkey (better known as Ringo Starr).

Write a program that reflects these changes and lets you practice
with the concept of lists. Your task is to:

    step 1: create an empty list named beatles;
    step 2: use the append() method to add the following members
            of the band to the list: John Lennon, Paul McCartney,
            and George Harrison;
    step 3: use the for loop and the append() method to prompt
            the user to add the following members of the band to
            the list: Stu Sutcliffe, and Pete Best;
    step 4: use the del instruction to remove Stu Sutcliffe and
            Pete Best from the list;
    step 5: use the insert() method to add Ringo Starr to the
            beginning of the list.

"""

beatles = list()  # step 1
# step 2
for i in range(3):
    beatles.append(input("Add John Lennon, Paul McCartney,"
                         "and George Harrison to the band: "))
print('The Beatles:', beatles)
# step 3

for i in range(2):
    beatles.append(input("Add Stu Sutcliffe, and Pete Best to the band: "))
print(beatles)
# step 4
i = -1
while i > -3:
    del(beatles[i])
    i -= 1
print('The Beatles:', beatles)
# step 5
beatles.insert(0, "Ringo Starr")
print('The Beatles:', beatles)
print("The Fab", len(beatles))
