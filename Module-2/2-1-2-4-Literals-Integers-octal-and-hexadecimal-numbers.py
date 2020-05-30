#!/usr/bin/python3
"""
Integers: octal and hexadecimal numbers

If an integer number is preceded by an 0O or 0o prefix (zero-o),
it will be treated as an octal value. This means that the number
must contain digits taken from the [0..7] range only.

0o123 is an octal number with a (decimal) value equal to 83.

Hexadecimal numbers. Such numbers should be preceded by the
prefix 0x or 0X (zero-x).

0x123 is a hexadecimal number with a (decimal) value equal
to 291. The print() function can manage these values too. Try this:
"""
print(0o123)
print(0x123)
