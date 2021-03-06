#!/usr/bin/python3
"""
Let's start by checking whether or not a variable created
outside any function is visible inside the functions.

In other words, does a variable's name propagate into a
function's body?

Look at the code in the editor. Our guinea pig is there.
"""


def myFunction():
    print("Do I know that variable?", var)


var = 1
myFunction()
print(var)


"""
The result of the test is positive - the code outputs:

Do I know that variable? 1
1

The answer is: a variable existing outside a function
has a scope inside the functions' bodies.

This rule has a very important exception. Let's try to find it.

Let's make a small change to the code:
"""


def myFunction1():
    var = 2
    print("Do I know that variable?", var)


var = 1
myFunction1()
print(var)


"""
The result has changed, too - the code produces a slightly
different output now:

Do I know that variable? 2
1

What's happened?

    the var variable created inside the function is not the same
    as when defined outside it - it seems that there two different
    variables of the same name; moreover, the function's variable
    shadows the variable coming from the outside world.

We can make the previous rule more precise and adequate:

A variable existing outside a function has a scope inside the functions'
bodies, excluding those of them which define a variable of the same name.

It also means that the scope of a variable existing outside a function
is supported only when getting its value (reading). Assigning a value
forces the creation of the function's own variable.

Functions and scopes: the global keyword

Hopefully, you should now have arrived at the following question: does
this mean that a function is not able to modify a variable defined outside
it? This would create a lot of discomfort.

Fortunately, the answer is no.

There's a special Python method which can extend a variable's scope in a
way which includes the functions' bodies (even if you want not only to
read the values, but also to modify them).

Such an effect is caused by a keyword named global:
global name
global name1, name2, ...

Using this keyword inside a function with the name (or names separated with
commas) of a variable(s), forces Python to refrain from creating a new
variable inside the function - the one accessible from outside will be used
instead.

In other words, this name becomes global (it has a global scope, and it
doesn't matter whether it's the subject of read or assign).

Look at the code in the editor.
"""


def myFunction2():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
myFunction2()
print(var)

"""
We've added global to the function.

The code now outputs:
Do I know that variable? 2
2

This should be sufficient evidence to show that the global keyword does
what it promises.

Now let's find out how the function interacts with its arguments.

The code in the editor should teach you something. As you can see,
the function changes the value of its parameter. Does the change
affect the argument?
"""


def myFunction3(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
myFunction3(var)
print(var)

"""
The code's output is:
I got 1
I have 2
1

The conclusion is obvious - changing the parameter's value
doesn't propagate outside the function (in any case, not
when the variable is a scalar, like in the example).

This also means that a function receives the argument's
value, not the argument itself. This is true for scalars.

Is it worth checking how it works with lists (do you recall
the peculiarities of assigning list slices versus assigning
lists as a whole?).

The following example will shed some light on the issue:
"""


def myFunction4(myList1):
    print(myList1)
    myList1 = [0, 1]


myList2 = [2, 3]
myFunction4(myList2)
print(myList2)

"""
The code's output is:
[2, 3]
[2, 3]

It seems that the former rule still works.

Finally, can you see the difference in the example below:
"""


def myFunction5(myList1):
    print(myList1)
    del myList1[0]


myList2 = [2, 3]
myFunction5(myList2)
print(myList2)

"""
We don't change the value of the parameter myList1
(we already know it will not affect the argument),
but instead modify the list identified by it.

The output may be surprising. Run the code and check:
[2, 3]
[3]

Can you explain it?

Let's try:

    if the argument is a list, then changing the value
    of the corresponding parameter doesn't affect the
    list (remember: variables containing lists are stored
    in a different way than scalars)
    but if you change a list identified by the parameter
    (note: the list, not the parameter!), the list will
    reflect the change.

"""
