"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
tup = ('business', 'finance', 'accounting')
print(f'The zero-th element of the tuple is "{tup[0]}"')
print(f'The elements 1 through 2 of the tuple are {tup[1:3]}')
print(f'The last element of the tuple is "{tup[-1]}"')

tup = ('business', 'finance', 'accounting')
tup1 = (1, 2, 3)
for n, m in zip(tup, tup1):
