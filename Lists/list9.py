"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
alist = ['accounting','finance','marketing','economics','management']
print(f"The original list is {alist}")
alist1 = alist[1:4]
print(f'The elements at indices 1, 2 and 3 are {alist1}')
alist1 = alist[1:-1]
print(f'The elements starting at index 1 and up to 1 from the end are {alist1}')
alist1 = alist[:3]
print(f'The elements from index 0 to index 2 are {alist1}')
alist1 = alist[2:]
print(f'The elements from index 2 to the end are {alist1}')
alist1 = alist[0:3:2]
print(f'Every other element from index 0 to index 2 are {alist1}')