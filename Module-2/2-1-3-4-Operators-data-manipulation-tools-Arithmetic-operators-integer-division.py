#!/usr/bin/python3
"""
Integer division can also be called floor division.
A // (double slash) sign is an integer divisional operator. It differs from
the standard / operator in two details:

- Its result lacks the fractional part
- it's absent (for integers), or is always equal to zero (for floats);
this means that the results are always rounded;
- It conforms to the integer vs. float rule

As you can see, integer by integer division gives an integer result.
All other cases produce floats.
"""
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
"""
This is very important: rounding always goes to the lesser integer.
"""
print(6 // 4)
print(6. // 4)
"""
The result is two negative twos. The real (not rounded) result is -1.5 in both
cases.However, the results are the subjects of rounding. The rounding goes
toward the lesser integer value, and the lesser integer value is -2, hence: -2
and -2.0.
"""
print(-6 // 4)
print(6. // -4)
