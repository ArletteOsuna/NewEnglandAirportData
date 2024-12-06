"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
dict1 = {x: x*x for x in range(1, 11)}
print(f"The dictionary is {dict1}")

dict2 = {x: x*x for x in range(1, 11) if x*x % 2 == 1}
print(f"The new dictionary is {dict2}")
