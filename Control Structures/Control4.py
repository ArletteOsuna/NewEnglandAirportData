"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

sales_tx= float(input("Enter the sales tax: "))

if sales_tx> .05:
    print("The sales tax is high--it is greater than 5 percent.")
elif sales_tx< .05:
    print("The sales tax is low--it is less than 5 percent.")
else:
    print("The sales tax is exactly 5 percent.")