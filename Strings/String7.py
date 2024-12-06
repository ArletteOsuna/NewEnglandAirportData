"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

string = "accounting and bookkeeping"
newString = '587235'
print("String starts with 'a' is:", string.startswith("a"))
print("String ends with '.' is:", string.endswith("."))
print("String is all letters is:", string.isalpha())
print("String is all numbers is:", newString.isdigit())
print("String in all uppercase is:", string.upper())
print("String with first letter capitalized is:", string.capitalize())
print("String with the o's replaced with t's is:", string.replace("o", "t"))
print("First occurrence of 'ing' is at index:", string.find('ing'))
print("Second occurrence of 'ing' is at index:", string.find('ing', 10))
print("String centered on a width of 50 is:", string.center(50))
print("String centered on a width of 50 is:", string.center(50, "*"))
print("String right-justified on a width of 50 is:", string.rjust(50, "*"))
print("String split at the spaces is:", string.split())
print("String joined with dashes is:", "-".join(string))
print("The count of 'o' in string is:", string.count('o'))
newString = "Accounting and BookKeeping"
print("String with cases swapped is:", newString.swapcase())
