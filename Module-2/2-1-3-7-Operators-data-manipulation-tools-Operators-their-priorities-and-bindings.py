#!/usr/bin/python3
"""
List of priorities

Priority 	Operator 	
1 	+, - 	unary
2 	** 	
3 	*, /, % 	
4 	+, - 	binary

Subexpressions in parentheses are always calculated first.
"""
print(2 + 3 * 5)
#the modulo operator uses left-sided binding
print(9 % 6 % 2)
#just the exponentiation operator uses right-sided binding
print(2 ** 2 ** 3)
print(2 * 3 % 5)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
