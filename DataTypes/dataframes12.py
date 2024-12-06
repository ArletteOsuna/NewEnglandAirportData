"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
import pandas as pd

data = {'apples': [150,175,200,125],
        'pears': [250, 135, 325, 645],
        'peaches and plums': [175, 150, 160, 200]}

df = pd.DataFrame(data, index=['Store 1','Store 2','Store 3','Store 4'])
print(f"The Original DataFrame is\n{df}")

bananas = [275, 450, 150, 175]
df.insert(0,'bananas', bananas)
print(f"\nThe New DataFrame is\n{df}")