"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import matplotlib.pyplot as plt

grades = [82, 72, 74, 98, 97, 88, 927, 83, 78, 62, 83, 41.08, 91.32, 82.62, 87, 80.26, 78, 96.88, 69.1, 88, 87.3, 87.37,
          90.74, 98.60, 87, 85, 43, 56, 73, 55, 54, 11, 20, 51, 79, 81, 27]
plt.hist(grades, bins=[0, 20, 40, 60, 80, 100], color='r')
plt.title("Histogram of Grades")
plt.xlabel('Marks')
plt.ylabel('No. of Students')
plt.show()
