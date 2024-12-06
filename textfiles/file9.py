"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import random

f = open("integers.txt", 'w')
for count in range(500):
    number = random.randint(0, 501)
    f.write(str(number) + '\n')
f.close()

print("The numbers in the file are:")
f = open("integers.txt")
for line in f:
    line = line.rstrip()
    print(line)

fhand = open('integers.txt')
theSum = 0
for line in fhand:
    line = line.strip()
    number = int(line)
    theSum += number
print(f"\nThe sum of the numbers is {theSum:,d}")