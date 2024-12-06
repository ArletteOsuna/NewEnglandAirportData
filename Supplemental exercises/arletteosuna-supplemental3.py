"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: Supplemental exercises Strings
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

print('Exercise #1')
# the purpose of this program is to print the word given backwards.
# a key feature is that each letter is on the same line

string = input('Enter a string: ')
print(f'The string, {string}, backwards, is {string[::-1]}')

print('\nExercise #2')
# the purpose of this program is to asks the user for a string. It then counts the number of
# letters, digits, and special symbols. Which is also a key factor.
string1 = input('Enter a sample string: ')

chars = 0
digits = 0
symbols = 0

for char in string1:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

print(f'The total count of chars, digits, and symbols in {string1}')
print(f'Characters = {chars}, Digits = {digits}, Symbols = {symbols}')

print('\nExercise #3')
# This program gives you a variety of options on how to change up the given string
# It shows you the word all capitalized, all lower case, parts of the word etc.

string = "Programming in Python"
length = len(string)
print(f'#1 Print the length of the string: {length}')
print(f'#2 Print the position where "in" appears the first time is: {string.find('in')} ')
print(f'#3 Print the number of times "n" appears is: {string.count('n')}')
print(f'#4 Print the number of spaces is: {string.count(' ')}')
print(f"#5 Print the substring 'Pro': {string[0:3]}")
print(f'#6 Print the substring "thon": {string[-4::]}')
print(f'#7 Print the substring "Programming in Py": {string[:-4]} ')
print(f'#8 Split the string at the spaces: {string.split()}')
print(f'#9 Print the substring "a": {string[5]}')
print(f'#10 Print the string in uppercase: {string.upper()}')
print(f'#11 Print the string in lowercase: {string.lower()}')
print(f'#12 Print the string but replace "in" with "with": {string.replace("in", "with")}')

print('\nExercise #4')
# This program will ask for two strings and input the second string in the middle
# of the first string. Length was used to split the word.

string2 = input('Enter a string: ')
string3 = input('Enter a string to go in the middle of the previous string: ')

# Math to split the word
middle = len(string2) // 2
first2 = string2[:middle]
last2 = string2[middle:]
middle = first2 + string3 + last2

print(f'The new string is {middle}')

print('\nExercise #5')
# This program asks for a string and then adjusts the word based on the number inputted
# It will rotate it to the left and to the right. The use of length is for when
# a number inputted is larger than the word count itself.
string4 = input('Enter a string: ')
characters = int(input('Enter number of characters to rotate--the number must be less than the number of characters '
                       'in the string: '))
# Loop inputted
while characters > len(string4):
    characters = int(input('Enter number of characters to rotate--the number must be less than the number of '
                           'characters in the string: '))

# Math for the left side
left = string4[characters:]
right = string4[:characters]
# Math for the right side
left1 = string4[-characters:]
right1 = string4[:-characters]

print(f'The string, {string4}, rotated to the left 5 characters is {left + right}')
print(f'The string, {string4}, rotated to the right 5 characters is {left1 + right1}')


print('\nExercise #6')
# The purpose of this program is to print out how many vowels the word/phrase
# inputted has. A key factor is the count giving you the outcome.
string5 = input('Enter a string: ')
# Naming out the vowels
vowels = ['a', 'e', 'i', 'o', 'u']
total = string5.count('vowels')

for i in string5:
    if i in vowels:
        total = total + 1
print(f"There are {total} vowels in the string '{string5}'")

print('\nExercise #7')
# The purpose of this program is to print out each letter inputted separate
# A key factor is the simplicity of this code using []
name = 'Arlette'
print(f'The string is "{name}"')
print(f'The character in position 0 is {name[0]}')
print(f'The character in position 1 is {name[1]}')
print(f'The character in position 2 is {name[2]}')
print(f'The character in position 3 is {name[3]}')
print(f'The character in position 4 is {name[4]}')
print(f'The character in position 5 is {name[5]}')
print(f'The character in position 6 is {name[6]}')

