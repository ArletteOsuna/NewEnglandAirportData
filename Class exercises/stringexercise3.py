"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

print(f" {'Inches':>8s}{'inches':>16s}{'kilometers':>16s}")
print(f'{"="*40}')

for num in range(1, 101):
    meters = num/39.67
    kilo = meters/1000
    print(f'{num:>8.2f}{meters:>14.2f}{kilo:>18,.6f}')
