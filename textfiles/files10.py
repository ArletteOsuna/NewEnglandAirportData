"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import random

with open('integers.txt', 'w') as f:
    for count in range(500):
        number = random.randint(0, 501)
        f.write(str(number) + '\n')

print("The numbers in the file are:")
f = open("integers.txt")
for line in f:
    line = line.rstrip()
    print(line)
