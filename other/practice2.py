"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
print("\nExercise 3: ")

input("Enter a positive number: ")
if numm == 0:
    num1 = range(2,(numm+1)*2,2)
    num2 = numm
    print("You entered", num1, "of 4 and", num2, "multiples of 8.")

principal = float(input('Enter principal: '))
rate = float(input('Enter interest rate: '))
years = float(input('Enter number of years: '))

simple = (principal * rate * years) / 100
total = simple + principal

print('The amount of interest is: ', simple)
print('The total amount owed is: ', total)