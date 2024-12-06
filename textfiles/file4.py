"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

fhand = open('mbox.txt')
# count = 0
loop = True
while loop:
    # count += 1
    # Get next line from file
    line = fhand.readline().rstrip()    # \n
    print(f"Line: {line}")
    # if line is empty, end of file is reached
    if not line:
        loop = False

print('\nAnother Use of readline()')
fhand = open('mbox.txt')
count = 0
loop = True
while loop:
    count += 1
    # Get next line from file
    line = fhand.readline().rstrip()    # line = fhand.readline().strip('\n')
    if line !='':
        print(f"Line: {line}")
    else:
        loop = False

