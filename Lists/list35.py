"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
string = eval(input('Enter a series of numbers, separated by commas: '))
print(string)
alist = list(string)
print(f"The list is {alist}")

print()
string = input('Enter a series of numbers, separated by spaces: ')
print(f"The numbers that were inputted are '{string}'")
items = string.split()
print(f"The items in a list are {items}")
blist = [float(x) for x in items]
print(f"The list is {blist}")
