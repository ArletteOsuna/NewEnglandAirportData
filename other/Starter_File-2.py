"""
Class: CS230--Section 1
Name: Arlette Osuna
Description: Quiz #1 Fall 2023 Programming Questions
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print(f"{'=' * 15} Question #1 {'=' * 15}")
print(f"{'=' * 12} List Manipulation {'=' * 12}")

gadgets = ['Mobile', 'Laptop', 100, 'Camera', 310.28, 'Speakers', 27.00, 250, 'Television', 1000, 'Laptop Case',
           'Camera Lens']
# type your code here
# Separate items into strings and numbers
string_items = [item for item in gadgets if isinstance(item, str)]
numeric_items = [item for item in gadgets if isinstance(item, (int, float))]

average_price = sum(numeric_items) / len(numeric_items)  # Calculate avg

print(f"The string items are {string_items}")
print(f"The numeric items are {numeric_items}")
print(f"The average price of the items is ${average_price:.2f}")

# Problem 2
print(f"\n\n{'=' * 15} Question #2 {'=' * 15}")
print(f"{'=' * 4} Writing a Dictionary to Text File {'=' * 4}")

dict1 = {
    'Emp1': {'name': 'Delaney Gunner', 'salary': 50000},
    'Emp2': {'name': 'Glory Posey', 'salary': 75000},
    'Emp3': {'name': 'Carrie Doran', 'salary': 40000},
    'Emp4': {'name': 'Alden Painter', 'salary': 30000},
    'Emp5': {'name': 'Drake Ash', 'salary': 150000},
    'Emp6': {'name': 'Bake Stone', 'salary': 10000},
}
# type your code here
for emp, details in dict1.items():
    if details['salary'] < 50000:
        details['salary'] *= 1.10  # increase salary by 10%

print(f"The updated dictionary is {dict1}")

with open('../updated_salaries.txt', 'w') as file:
    for details in dict1.values():
        file.write(f"{details['name']}: ${details['salary']:.2f}\n")

print("The name and updated salary have been written to a file")
