#!/usr/bin/python3
"""
The inner life of lists

Now we want to show you one important, and very surprising, feature of lists,
which strongly distinguishes them from ordinary variables.

We want you to memorize it - it may affect your future programs, and cause
severe problems if forgotten or overlooked.

Take a look at the snippet in the editor.

The program:

- creates a one-element list named list1;
- assigns it to a new list named list2;
- changes the only element of list1;
- prints out list2.

The surprising part is the fact that the program will output: [2], not [1],
which seems to be the obvious solution.

Lists (and many other complex Python entities) are stored in different ways
than ordinary (scalar) variables.

You could say that:

- the name of an ordinary variable is the name of its content;
- the name of a list is the name of a memory location where the list is
  stored.

Read these two lines once more - the difference is essential for
understanding what we are going to talk about next.

The assignment: list2 = list1 copies the name of the array, not its
contents. In effect, the two names (list1 and list2) identify the same
location in the computer memory. Modifying one of them affects the other,
and vice versa.

How do you cope with that?
"""

list1 = [1]
list2 = list()
list2 = list1
list1[0] = 2
print(list2)
