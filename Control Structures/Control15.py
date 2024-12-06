"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
# Better python code
total = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    total += number
    data = input("Enter a number or just enter to quit: ")
print("The sum is", total)

