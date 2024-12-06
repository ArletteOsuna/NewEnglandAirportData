"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
count = 1
while guess != number:
    if guess > number:
        print("Your guess is too high!")
        guess = int(input("Guess a number between 1 and 100: "))
        count += 1
    else:
        print("Your guess is too low!")
        guess = int(input("Guess a number between 1 and 100: "))
        count += 1

print(f"You are correct! The number is {guess}")
print(f"It took you {count} times to get the answer right.")



