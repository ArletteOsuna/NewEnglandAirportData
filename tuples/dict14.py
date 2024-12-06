"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

dict1 = {"course1": {"name": "CS150", "prof": "Smith"},
              "course2": {"name": "CS230", "prof": "Jones"},
              "course3": {"name": "IT101", "prof": "Samuels"}}
print(f"The dictionary is {dict1}\n")

for course in dict1.keys():
    name = dict1[course]["name"]
    prof = dict1[course]["prof"]
    print(f"The professor for {name} is {prof}")

# who teaches CS230 ?
for course in dict1.keys():
    if dict1[course]["name"] == "CS230":
        name = dict1[course]["name"]
        prof = dict1[course]["prof"]
        print(f"\nThe professor for {name} is {prof}")
