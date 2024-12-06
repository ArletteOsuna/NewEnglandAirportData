"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import matplotlib.pyplot as plt     # importing matplotlib library

x = range(1,51)
y = [num ** 2 for num in range(1,51)]

plt.plot(x,y,color='green', linestyle='dashed', linewidth=3)                    # plotting x and y
plt.show()
