"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import matplotlib.pyplot as plt

data = {'Northeast': 230, 'South': 850, 'Mid-Atlantic': 720, 'Midwest': 430, 'West': 520}
days = list(data.keys())
values = list(data.values())
plt.xlabel('Amounts')
plt.ylabel('Regions')
plt.title('Sales')
plt.barh(days, values, color='maroon')
plt.show()
