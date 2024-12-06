"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

total = 0.0
loop = True
while loop:
    data = input("Enter a number or just enter to quit: ")
    if data == "":
        loop = False
    else:
        number = float(data)
        total += number
print("The sum is", total)