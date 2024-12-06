"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import matplotlib.pyplot as plt

regions = ['Northeast', 'South', 'Mid-Atlantic', 'Midwest', 'West']
sales = [230, 850, 720, 430, 520]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'aquamarine']
plt.title("Sales by Region")
plt.pie(sales, explode=[0, 0, 0, .2, 0], colors=colors,labels=regions,autopct='%1.2f%%')
plt.show()
