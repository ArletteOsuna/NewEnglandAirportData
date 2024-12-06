"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

print("Exercise 1")
alist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
length = len(alist)
string = "Enter a number between 0 and " + str(length) + ": "
num = int(input(string))
sub1 = alist[:num]
sub2 = alist[-num:]
print("The substring of the list between 0 and", num,"is",sub1)
print("The substring of the list between the end of the list and", num,"is",sub2)
