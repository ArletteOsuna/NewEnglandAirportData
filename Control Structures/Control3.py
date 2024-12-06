"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

sales_tax = float(input("Enter the sales tax: "))

if sales_tax> .05:
    print("The sales tax is high--it is greater than 5 percent.")
else:
    print("The sales tax is low--it is less than or equal to 5 percent.")
