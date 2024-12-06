"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
fhand = open('text1.txt')
search = input('Enter letter to be searched: ')
find = find(search)
print(f'Occurrences of {search}: {find}')

print(f'Occurrences of bank spaces: ')

print(f'The total number of time python appears in the file is: {}')

letter =
with open('text1.txt') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in 1:
 """
color = ['red', 'green', 'white', 'black', 'pink', 'yellow']
file_name = 'colors.txt'

with open(file_name, 'w') as file:
    file.write(''.join(color))

print(f'Colors written to {file_name}.')
