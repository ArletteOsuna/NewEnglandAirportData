"""Class: CS230--Section 1
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import math

radius = float(input('Enter the radius: '))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print('The circumference is: ', round(circumference, 2))

print('The area is: ', round(area, 2))
