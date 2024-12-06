"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

command = '1'

match command:
    case 1 | '1':
        print('Selected 1')
    case 0 | '0' | 'Q':
        print('Quit')
    case _:
        print('Unknown command')
