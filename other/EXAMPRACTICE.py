"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

s = "Bentley university, waltham ma"
result = ""
for ch in s:
    if ch.isUpper():
        result += ch.supper()
    else:
        result += ''
print(result)
"""
firstName = 'Tom'
lastName = 'Brady'
code = firstName[0:2] + lastName[1] + lastName[4]
code = code.upper()
print(code)

for num in range(10, 21, 2):
    print(num, end='')

print('\nhello')
first = input("Enter your first name: ")
last = input("Enter your last name: ")
college = input("Enter your college name: ")
mascot = input("Enter your college mascot: ")
email = first[0] + last.lower() + "@" + mascot.lower() + "." + college.lower() + ".edu"
print(f"Your email address is {email}")

print("\nexample")

hours = input("Enter the number of hours: ")
parking = 15
additionalParking = 10
if hours <= 3:
    print(f"The cost to park {hours} is {parking * hours}")
else:
    print(f"The cost to park {hours} is {total}")

"""


