#!/usr/bin/python3
"""
Shifting a value one bit to the left thus corresponds
to multiplying it by two; respectively, shifting one
bit to the right is like dividing by two (notice that
the rightmost bit is lost).
"""
var = 17
varLeft = var << 2
varRight = var >> 1
print(var, varLeft, varRight)
