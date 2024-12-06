"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Supplemental exercise 2)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

print("Exercise 1:")
# In this exercise you are shown how to display odd numbers and multiples of 10.
# It shows you different ranges and which equations display certain outcomes.

print("The first 10 odd numbers are: ")
for num in range(0, 20):
    if num % 2 != 0:
        pass
        print(num)

print("The first five multiples of 10 are:")
for num1 in range(10, 60):
    if num1 % 10 == 0:
        pass
        print(num1)

print("\nExercise 2:")
# The purpose of this exercise is to calculate the sum of numbers
# from one to the chosen number. A key component is the formula used with range.

num = int(input("Enter a number: "))
total = sum(range(1, num + 1))
print("The total is: ", total)

print("\nExercise 3:")
# The purpose of this program is to ask the user for positive numbers and then count
# The multiples of the number given. A key feature is the summary given at the end.
status = True
m4 = 0
m8 = 0

while status:
    numm = int(input("Enter a positive number: "))
    if numm > 0:
        if numm % 4 == 0:  # to find multiple of 4
            m4 += 1
        if numm % 8 == 0:  # to find multiple of 8
            m8 += 1

    elif numm == 0:
        status = False

print("You entered", m4, "multiples of 4 and", m8, "multiples of 8.")

print("\nExercise 4:")
# The purpose of this program is create a loop of a sequence. A key component is
# the numbers given in the range and the output.

for i in range(12, 90, 11):  # loop sequence
    print(i, end=", ")

print("\nExercise 5:")
# The purpose of this program is to add the multiples of three from the total numbers
# of 1 to 100. The multiples given are the ones of three or five.

total = 0
for i in range(1, 101):  # range to 101 so that 100 is included
    if i % 3 == 0 or i % 5 == 0:
        total += i

print("The total of the numbers from 1 to 100 that are multiples of three or five is", total)

print("\nExercise 6:")
# The purpose of this program is to convert temperature. The program asks the user whether
# they want Celsius or Fahrenheit. With that information it converts it and asks again
# until the user has stated no to continue.

flag = True
c = 0
f = 0
convert = input("Do you want to convert Fahrenheit to Celsius [f] or Celsius to Fahrenheit [c]? ")
temperature = float(input("Enter the temperature: "))
while flag:

    if convert == "c":
        f = (9 / 5 * temperature) + 32  # formula for Fahrenheit
        print("The Celsius temperature", temperature, "in Fahrenheit is", f)

    if convert == "f":
        c = 5 / 9 * (temperature - 32)  # formula for Celsius
        print("The Fahrenheit temperature", temperature, "in Celsius is", c)

    conversions = input("Do you want to make any more temperature conversions [y]es or [n]o? ")

    if conversions == "y":  # continuation of loop
        convert = input("Do you want to convert Fahrenheit to Celsius [f] or Celsius to Fahrenheit [c]? ")
        temperature = int(input("Enter the temperature: "))
    elif conversions == "n":  # end of loop
        print("Thank you for using our temperature converter!")
        flag = False
