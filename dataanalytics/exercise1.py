"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import matplotlib.pyplot as plt

data = {'Java': 100, 'Python': 150, 'PHP': 75, 'JS': 85, 'C#': 95, 'C++': 50}
days = list(data.keys())
values = list(data.values())
plt.xlabel('Languages')
plt.ylabel('Number of Students')
plt.title('Popularity of Programming Language')
plt.bar(days, values, color ='GREEN')
plt.show()
