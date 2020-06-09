#!/usr/bin/python3
"""
Traditional way of doing the swap:
"""
variable1 = 1
variable2 = 2

auxiliary = variable1
variable1 = variable2
variable2 = auxiliary

"""
Python offers a more convenient way of doing the swap - take a look:
"""
variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1
