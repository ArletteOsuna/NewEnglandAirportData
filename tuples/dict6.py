"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
dict1 = {1: 'finance', 2: 'accounting', 3: 'economics'}
print(f"The original dictionary is {dict1}")
print(f"The value at key=1 is {dict1.get(1)}")
print("\nPrinting Keys")
for key in dict1. keys():
    print(f"Key: {key}")
for key in dict1:
    print(f"Key: {key}")
print("\nPrinting Values")
for value in dict1.values:
    print(f"Value: {value}")
print("\nPrinting Items")