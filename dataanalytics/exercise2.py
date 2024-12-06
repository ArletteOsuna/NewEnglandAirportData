"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import matplotlib.pyplot as plt

activities = ['eat', 'sleep’, 'work', 'play']
slices = [3, 7, 8, 6]
plt.pie(slices, explode=[0, 0, 0, .2, 0], labels=activities, autopct='%1.2f%%')
plt.show()
