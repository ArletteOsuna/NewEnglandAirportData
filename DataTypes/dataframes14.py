"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import pandas as pd

data = {'Original': ['financial',175,200,125],
        'Dataframe': [250, 135, 325, 645],
        'New Dataframe': [175, 150, 160, 200]}

df = pd.DataFrame(data, index=['0','1','2','3'])
print(f"The Original DataFrame is\n{df}")

#df.pop('peaches and plums')
#print (f"\nDeleting the last column using POP:\n{df}")
