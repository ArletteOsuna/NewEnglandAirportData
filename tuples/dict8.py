"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
dict1 = {1: 'finance', 2: 'accounting', 3: 'economics'}
print(f"The original dictionary is {dict1}")
# using pop to return and remove key-value pair.
popElement = dict1.pop(1)
print(f"The value removed is {popElement}")
print(f"The original dictionary is {dict1}")

dict2 = {1: 'finance', 2: 'accounting', 3: 'economics'}
print(f"\nThe original dictionary is {dict2}")
popElement = dict2.popitem()
print(f"The value removed is {popElement}")
print(f"The original dictionary is {dict2}")
