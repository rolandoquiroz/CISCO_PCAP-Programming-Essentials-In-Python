#!/usr/bin/python3
"""
Spathiphyllum, more commonly known as a peace lily or white sail plant,
is one of the most popular indoor houseplants that filters out harmful
toxins from the air. Some of the toxins that it neutralizes include benzene,
formaldehyde, and ammonia.

Imagine that your computer program loves these plants.
Whenever it receives an input in the form of the word Spathiphyllum,
it involuntarily shouts to the console the following string:
"Spathiphyllum is the best plant ever!"

Test Data

Sample input: spathiphyllum

Expected output: No, I want a big Spathiphyllum!

Sample input: pelargonium

Expected output: Spathiphyllum! Not pelargonium!

Sample input: Spathiphyllum

Expected output: Yes - Spathiphyllum is the best plant ever!
"""
word = input("Please input your string: ")

if word == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif word == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not " + word + "!")
