"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
print('\nEasiest way to read in lines from a file')
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    print(f'\t{line}')
