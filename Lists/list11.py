"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
alist = ['accounting', 'economics', 'finance', 'management','finance']
print(f"The original list is {alist}")
alist.remove('finance')
print(f"\nThe new list is {alist}")

item = alist.pop(1)
print(f'The item removed is "{item}"')
print(f"The new list is {alist}")

del(alist[1])
print(f"The new list is {alist}")
