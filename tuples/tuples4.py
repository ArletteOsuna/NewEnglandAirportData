"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
tup = ('business','finance', 'accounting', 'finance')
print(f'Is any element of the tuple True? {any(tup)}')
print(f'The number of times "finance" appears: {tup.count("finance")}')
print(f'The smallest major: (min(tup)}')
print(f' The largest major: {max(tup)}')
print(f'The length of tuple: {len (tup)}')

numbers = (1, 2, 3, 6)
twoTuples = tup + numbers
print(f"\nConcatenating two tuples {twoTuples}")