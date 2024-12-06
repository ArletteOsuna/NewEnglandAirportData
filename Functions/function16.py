"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """


def new_func():
    global num
    num = num * 2
    num2 = num
    print(f"Inside function {num = }")
    print(f"Inside function {num2 = }")


num = 75
new_func()
