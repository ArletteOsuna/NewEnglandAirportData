"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
alist = ['accounting', 'management','finance','economics']
alist.sort()
print(f'The list sorted in ascending order is {alist}')

alist = ['accounting', 'management','finance','economics' ]
alist.sort(reverse=True)
print(f'The list sorted in descending order is {alist}')

alist = ['accounting', 'marketing','finance','economics' ]
alist.sort(key=len)
print(f'Sorted list according to length: {alist}')

alist = ['accounting', 'marketing','finance','economics' ]
alist.sort(key=len, reverse=True)
print(f'Sorted list according to length, revers order: {alist}')

'''alist = ['apple', 'banana', 'kiwi', 'orange', 'grapefruit', 1, 3, 4]
alist.sort()
print(f'\nThe list sorted in ascending order is {alist}')'''

