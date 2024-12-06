"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

for num in range(10, 20):       # to iterate between 10 to 19
    for i in range(2, num):     # to iterate on the factors of the number
        if num % i == 0:        # to determine the first factor
            j = num / i         # to calculate the second factor
            print(num, 'equals', i, "*", j)
            break               # move to the next number in the 1st for
    else:                       # else part of the loop
        print(num, 'is a prime number')