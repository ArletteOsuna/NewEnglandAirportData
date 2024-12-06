"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

for num in range(21):  # for loop
    if num % 5 == 0:
        continue
    print("The number is", num)

print()
num2 = 21  # while loop
while num2 >= 0:
    num2 -= 1
    if num2 % 5 == 0:
        continue
    print("The number is", num2)

print("\nDone!")
