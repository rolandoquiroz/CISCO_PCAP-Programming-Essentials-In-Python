#!/usr/bin/python3
"""
sep='separator' Optional. Specify how to separate the objects, if there is
more than one. Default is ' '
end='end' Optional. Specify what to print at the end. Default is '\n'
(line feed)

In a function any keyword arguments (like sep and end in this caso) have to
be put after the last positional argument (this is very important)
"""
print("My name is", "Python.")
print("Monty Python.")
print()

print("My name is", "Python.", sep=' ', end='\n')
print("Monty Python.", end='\n')
print(end='\n')

print("My name is", "Python.", sep='xxx', end='333')
print("Monty Python.", end='&&&')
print(end='###')

print()
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="#", end="$\n")
