"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

num = int(input("Enter number of items: "))

if num >= 0 and num <= 50:
    price = 100.00
    total = price * num
    print("The total cost is", total)
else:
    price = 90.00
    total = price * num
    print("The total cost is", total)

