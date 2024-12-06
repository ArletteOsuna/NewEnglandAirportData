"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

print("\nExercise 1: Temperature Conversion")
# This program converts a temperature given in Celsius to both Fahrenheit and Kelvin.
# It calculates the temperature inputted automatically.

C = int(input("Enter Celsius temperature: "))

F = (9 / 5 * C) + 32
K = C + 273.15

print("The Celsius temperature of", C, "is", F, "degrees Fahrenheit")
print("The Celsius temperature of", C, "is", K, "degrees Kelvin")

print("\nExercise 2: Total Pay")
# The purpose of this program is to calculate the total weekly pay.
# A unique feature is that it also calculates overtime pay.
# A key feature is its accuracy on providing the total weekly pay.

Hourly = float(input("Enter the hourly wage: "))
Overtime = int(input("Enter the overtime hours: "))

Weekly = (40 * Hourly) + (1.5 * Hourly * Overtime)

print("The employee's weekly pay is $", round(Weekly, 2),)

print("\nExercise 3: Total of Digits")
# The purpose of this program is to provide the sum of the four-digit inputted, converting digits to integers.
# A key feature is that it looks at each number inputted individually and interprets it into the sum.

digits = (input("Enter a four-digit number: "))

a = int(digits[0])
b = int(digits[1])
c = int(digits[2])
d = int(digits[3])

digits_sum = a + b + c + d
print("The sum of the digits in", digits, "is", digits_sum)

print("\nExercise 4: Slices")
# The purpose of this program is to make splitting a pizza easier. It calculates the number of guests included in
# the split and gives you two options. One option splits it evenly ignoring the leftovers.
# The other option gives everyone the same amount while including the split of the leftovers. A key feature is that
# it provides you with two options, giving you options to pick from using basic division.

guests = int(input('Number of guests: '))

option1 = int(32 / guests)
leftover = 32 % guests
option2 = float(32 / guests)

print('Option 1:', option1, 'slices each,', leftover, 'left over')
print('Option 2:', option2, 'slices each')

print("\nExercise 5:Total ")
# The purpose of this program is to give you a total of the integer given, giving you knowledge in basic arithmetic.
# A key feature is that it uses basic addition and handles user input.

n = int(input('Enter a number: '))

nn = n * 10 + n
nnn = nn * 10 + n
total = int(n + nn + nnn)
print('The result is:', total)
