"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

print("\nNested Lists")
alist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'The original list {alist}')
print('\nThe flattened list:')
for list in alist:
    for number in list:
        print(number, end=' ')