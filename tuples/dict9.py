"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

seq = {'finance', 'accounting', 'economics'}
# initializing with None
dict1 = dict.fromkeys(seq)
print(f"The dictionary with None values: {dict1}" )
# using fromkeys() to convert sequence to dict initializing with 1
dict2 = dict.fromkeys(seq, 1)
print(f"The newly created dictionary with 1 as value: {dict2}")
