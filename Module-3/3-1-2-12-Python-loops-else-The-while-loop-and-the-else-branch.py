#!/usr/bin/python3
"""
Both loops, while and for, have one interesting (and rarely used) feature.

As you may have suspected, loops may have the else branch too, like ifs.

The loop's else branch is always executed once,
regardless of whether the loop has entered its body or not.
"""
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
