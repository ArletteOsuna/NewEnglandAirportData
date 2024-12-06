"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Supplemental exercise on lists --See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
print('Exercise #1')
# The purpose of this is to sum all numbers in a list except those between a 6 and the next 7.
# A key feature is handling sections of numbers that are ignored.

numbers = [1, 1, 6, 5, 5, 3, 8, 7, 2, 90]
print(f'The original list is {numbers}')
if 6 in numbers and 7 in numbers:
    index6 = numbers.index(6)
    index7 = numbers.index(7)
    del numbers[index6:index7 + 1]  # deleted numbers between 6 and 7
    print(numbers)

total = 0
# the total of the numbers
for num in numbers:
    total += num

print(f'The total is {total}')

print('\nExercise #2')
# The purpose of this is to create a list of random integers and calculate the difference between the maximum and minimum values.
# A key feature is calculating the range between the largest and smallest numbers in the list.

import random

alist = []
num = 10
for x in range(num):  # random numbers
    number = random.randint(1, 100)
    alist.append(number)
greatest = max(alist)
lowest = min(alist)
difference = greatest - lowest  # subtracting the max and min
print(f'The list is {alist}')
print(f'The difference between {greatest} and {lowest} is {difference}')

print('\nExercise #3')
# The purpose of this is to calculate the difference between corresponding elements in two lists and track the sum of their squared differences.
# A key feature is iterating through both lists simultaneously and computing cumulative squared differences.

alist = [0.1, 0.0, 0.4, 5.6, 8.9]
alist2 = [0.2, 0.5, 0.6, 10.2, 7.89]

squared = 0

print(f'The first list is {alist}.')
print(f'The second list is {alist2}.\n')
#  squaring the number
for a, b in zip(alist, alist2):
    difference = a - b
    squared_difference = difference ** 2
    squared += squared_difference
    # Print the difference for each element pair
    print(f'Difference is: {difference:.3f}')

print(f'\nThe sum of the difference squared is: {squared:.3f}')

print('\nExercise #4')
# The purpose of this is to allow a user to remove duplicates in a list by specifying one of the duplicated values.
# A key feature is to use a function that removes all instances of a given duplicate value.

alist3 = [5, 200, 15, 25, 200, 25, 50, 200, 25, 15]
print(f'The list is {alist3}')
num = int(input('Enter a number that is duplicated to be removed from the list: '))

blist = [x for x in alist3 if x != num]  # removes duplicates
print(f'The updated list is {blist}')

print('\nExercise #5')
# The purpose of this is to identify nested lists within a list and print each nested list.
# A key feature is checking if an element is a list and outputting it accordingly.

alist4 = [[5, 6], 6, [4, 9, 10], 8, 10]
print(f'The original list is {alist4}')
print(f'The nested list is {alist4[0]}')  # Will execute the first nested list
print(f'The nested list is {alist4[2]}')


print('\nExercise #6')
# The purpose of this is to assign grades based on a grading scheme that uses the highest score as a reference.
# A key feature is the dynamic grading scale, where each student's grade depends on their score's proximity to the highest score.

grades = input('Enter a series of grades, seperated by a comma: ')
grades_list = [int(grade.strip()) for grade in grades.split(',')]  # lists the grade seperated by a comma
print(f'The list is {grades_list}')

best = max(grades_list)
count = 0  # to count each student
for student_grade in grades_list:
    if student_grade >= best - 10:
        grade = 'A'
    elif student_grade >= best - 20:
        grade = 'B'
    elif student_grade >= best - 30:
        grade = 'C'
    elif student_grade >= best - 40:
        grade = 'D'

    print(f'The grade of student{count} is {grade}')
    count += 1
