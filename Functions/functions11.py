"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """


def arithmetic_sum(*nums):
    total = 0
    for x in nums:
        total += x
    return total


print(f"{arithmetic_sum(45, 32, 89, 78):.2f}")
print(f"{arithmetic_sum(880.95, 995.23, 345, 150.263, 965.47):.2f}")
print(f"{arithmetic_sum(45.5, 32):.2f}")
print(f"{arithmetic_sum(45):.2f}")
print(f"{arithmetic_sum():.2f}")
