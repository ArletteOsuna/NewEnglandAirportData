"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """


def arith(num1, num2):
    total = num1 + num2
    diff = num1 - num2
    return total, diff


num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
total, diff = arith(num1, num2)
print(f'The total of the two numbers is {total}')
print(f'The difference between the numbers is {diff}')

print(type(arith(num1, num2)))