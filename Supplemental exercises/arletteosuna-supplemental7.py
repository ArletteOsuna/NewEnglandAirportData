"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Supplemental exercise on Dictionaries)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

print('Exercise #1')
# The purpose of this program is to create a dictionary where keys are first characters and values are words.
input_string = input("Enter a string: ")
result = {}

words = input_string.split()  # Split the string into words
for word in words:
    first_char = word[0]  # Use the first character as the key
    if first_char not in result:
        result[first_char] = [word]
    else:
        result[first_char].append(word)

for key in result:
    print(f"{key}: {result[key]}")

print('\nExercise #2')
# The purpose of this program is to combine two lists into a dictionary based on ages.
names = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

age_dict = {}
for i in range(len(names)):
    name = names[i]
    age = ages[i]
    if age not in age_dict:
        age_dict[age] = [name]
    else:
        age_dict[age].append(name)

print(age_dict)

print('\nExercise #3')
# The purpose of this program is to sort and analyze professor names from a dictionary.
professors = {
    "CS230": ["Bernstein", "Jones", "Prentice"],
    "CS150": ["Ganfield", "Sullivan", "Connors"],
    "CS213": ["Sinema", "McSally"],
    "CS350": ["Feinstein", "Loudermilk"]
}

# Combine all professor names into one list
all_names = []
for name_list in professors.values():
    for name in name_list:
        all_names.append(name)

# Sort names alphabetically
sorted_names = sorted(all_names)

# Longest name
longest_name = ""
for name in all_names:
    if len(name) > len(longest_name):
        longest_name = name

print(f"The list of names sorted is {', '.join(sorted_names)}")
print(f"The longest name is {longest_name}")

print('\nExercise #4')
# The purpose of this program is to validate login credentials using a dictionary.
# Dictionary of users and passwords
users = {'User1': '123Password', 'User3': 'Password123', 'User5': '123P!'}

username = 'User3'
password = 'Password123'

# Check if the username exists and the password matches
if username in users and users[username] == password:
    print(f"The dictionary of users and passwords is {users}")
    print("The login was successful")
else:
    print(f"The dictionary of users and passwords is {users}")
    print("login failed...")

# Failed password attempt:
username = 'User5'
password = 'wrongpass'

# Check if the username exists and the password matches
if username in users and users[username] == password:
    print(f"The dictionary of users and passwords is {users}")
    print("The login was successful")
else:
    print(f"The dictionary of users and passwords is {users}")
    print("login failed...")
