#!/usr/bin/python3
"""
Your task here is even more special than before:
you must redesign the (ugly) vowel eater from the previous
lab (3.1.2.10) and create a better, upgraded (pretty)
vowel eater! Write a program that uses:

    a for loop;
    the concept of conditional execution (if-elif-else)
    the continue statement.

Your program must:

    ask the user to enter a word;
    use userWord = userWord.upper() to convert the word
    entered by the user to upper case; we'll talk about
    the so-called string methods and the upper() method
    very soon - don't worry; use conditional execution
    and the continue statement to "eat" the following
    vowels A, E, I, O, U from the inputted word;
    assign the uneaten letters to the wordWithoutVovels
    variable and print the variable to the screen.

Look at the code in the editor. We've created wordWithoutVovels
and assigned an empty string to it. Use concatenation operation
to ask Python to combine selected letters into a longer string
during subsequent loop turns, and assign it to the wordWithoutVovels
variable.

Test your program with the data we've provided for you.

Test data

Sample input: Gregory

Expected output:
GRGRY

Sample input: abstemious

Expected output:
BSTMS

Sample input: IOUEA

Expected output:
"""
wordWithoutVovels = ""
# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input('Please enter a word: ')
userWord = userWord.upper()

for letter in userWord:
    # Complete the body of the for loop.
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        wordWithoutVovels += letter

print(wordWithoutVovels)
