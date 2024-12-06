"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

import random

num = random.random()
print(num, "\n")

minimum = 1
maximum = 100
for roll in range(10):
    num = minimum + random.random() * (maximum - minimum)
    print(round(num, 3), end='  ')
