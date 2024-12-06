"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import matplotlib.pyplot as plt

data = [230, 850, 720, 430, 520]
labels = ['Northeast', 'South', 'Mid-Atlantic', 'Midwest', 'West']
plt.xticks(range(len(data)), labels)    # create a range from 0 through 5 and label the tick marks with the labels list
plt.xlabel('Regions')
plt.ylabel('Amounts')
plt.title('Sales')
plt.bar(range(len(data)), data,color='maroon')
plt.show()
