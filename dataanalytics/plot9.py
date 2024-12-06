"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import matplotlib.pyplot as plt

data1 = [23, 85, 72, 43, 52]
data2 = [42, 35, 21, 16, 9]
width = 0.4
t = list(range(len(data1)))
t1 = [x - (width/2) for x in t]
t2 = [x + (width/2) for x in t]
labels = ['Northeast', 'South', 'Mid-Atlantic', 'Midwest', 'West']
plt.xticks(range(len(data1)), labels)
plt.xlabel('Regions')
plt.bar(t1, data1, color='#ff8000',width=width, label='North')
plt.bar(t2, data2, color='r',  width=width, label='South')
plt.title("Numbers")
plt.legend(loc="best")
plt.show()
