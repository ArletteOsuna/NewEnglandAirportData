"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

"""
count = 0
number = input("Enter a number: ")
while number:
    if number == 1:
        count += 1
        print(f"You entered {count} numbers before 1")
    else:
        number = input("Enter a number: ")


count = 0
number = input("Enter a number: ")
while n != 1:
   count += 1
   number = input("Enter a number: ")
   
print(f"You entered {count} numbers before 1")

print("\nProblem 2:")

flavor = input("Enter a flavor: [vanilla] or [carrot]: ")
people = int(input("How many people?: "))
if people >= 14:
    if flavor == "vanilla":
        print("A vanilla round cake costs $8")
    elif flavor == "carrot":
        print("A carrot round cake costs $14")
elif people <= 20:
    if flavor == "vanilla":
        print("A vanilla sheet cake costs $18")
    elif flavor == "carrot":
        print("A carrot sheet cake costs $29")
elif people > 20:
    print("You need more than one cake")

for num in range(1,8):
    print(f"{num} divided by 7 is: {num/7:.4f}")
    

gpa = float(input("Enter your gpa: "))
state = input("Enter your state: ")
if state == 'NH':
    if gpa >= 3.7:
        print("You are eligible for the New Hampshire Scholarship")
elif gpa >= 3.7:
    print("You are eligible for the General Scholarship")
elif gpa < 3.7:
    print("You are not eligible for any Scholarship")

s = 'bread and muffins'
print(s[10:16])

integer = input("Please enter one integer at a time: ")
if integer % 3 == 0:
    print(integer," is a multiple  of 3")
elif integer == -1:
    print('')
else:
    print(integer, "is not a multiple of 3")
// 
for num in range(1, 8):
    print(f"{num} divided by 7 is: {num/7:.4f}")
count = 0
number = int(input("Enter a number: "))

while number != 1:
    count += 1
    number = int(input("Enter a number: "))

print(f"You entered {count} numbers before 1")

integer = int(input("Please enter one integer at a time: "))

if integer % 3 == 0:
    print(integer, "is a multiple of 3")
elif integer == -1:
    print('')
else:
    print(integer, "is not a multiple of 3")
"""
small_numbers = [1, 2, 3, 4]
numbers = []
for j in small_numbers: numbers.append(j * 2)
print(numbers)

numbers = [j * 2 for j in small_numbers]
print(numbers)