"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
fhand = open('mbox.txt')
lines = fhand.readlines()
print('\nResult of readlines() -> a list')
print(lines)
print('\nConverting the list to strings')
for line in range(len(lines)):
    sentence = lines[line].rstrip()
    print(f'\t{sentence}')