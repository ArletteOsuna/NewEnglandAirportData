"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

keys = [1,2,3,4]
values = ['finance','marketing','business','management']
# but this line shows dict comprehension here
print(list(zip(keys,values)))
dict1 = {k:v for (k,v) in zip(keys, values)}
print(f"The dictionary is {dict1}")
