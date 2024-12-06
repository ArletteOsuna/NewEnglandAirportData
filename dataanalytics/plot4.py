"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import matplotlib.pyplot as plt

yAxis = [5, 10, 15, 20, 25]
xAxis = [1, 2, 3, 4, 5]
plt.bar(xAxis, yAxis)
plt.show()

yAxis = [5, 10, 15, 20, 25]
xAxis = [1, 2, 3, 4, 5]
plt.bar(xAxis, yAxis, width=.5)
plt.show()
