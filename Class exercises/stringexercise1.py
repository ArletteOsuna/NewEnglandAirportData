"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

string = input("Enter a string: ")
length = len(string)
if length < 2:
    print("operation cannot be processed")
else:
    string2 = input("Enter a second string: ")
    newString = string[0:2] + string2[-2:]
    print("The new string is", newString)





