#!/usr/bin/python3
"""
The loop's body won't be executed here at all.
Note: we've assigned the m variable before the loop.

When the loop's body isn't executed,
the control variable retains the value it had before the loop.

Note: if the control variable doesn't exist before the loop starts,
it won't exist when the execution reaches the else branch.
"""
m = 111
for m in range(2, 1):
    print(m)
else:
    print("else:", m)


for i in range(5):
    print(i)
else:
    print("else:", i)
