"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
dict1 = {'A': 100, 'B': 540, 'C': 239, 'D': 650}
multiplied_dict = {key: value * 3 for key, value in dict1.items()}
print(f"Each item in the dictionary multiplied by three: {multiplied_dict}")

print("\nDictionary methods")
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

newDict = {}
for i in range(len(keys)):
    newDict[keys[i]] = values[i]
print('The new dictionary is', newDict)

orgDict = {"Day1": "S001", "Day2": "S002", "Day3": "S001", "Day4": "S005", "Day5": "S005", "Day6": "S009",
           "Day7": "S007"}
uniqueList = []
for i in orgDict.values():
    if i not in uniqueList:
        uniqueList.append(i)
print(uniqueList)


print("\nlist of dictionaries")
bankOfAmerica = [
    {"address": "880 Main Street", "phone": "781-642-7254", "ATM": "Drive-Thru"},
    {"address": "578 South Street", "phone": "844-401-8500", "ATM": "Walk-Up"},
    {"address": "248 Moody Street", "phone": "844-401-8500", "ATM": "Walk-Up"},
    {"address": "625 South Street", "phone": "844-401-8500", "ATM": "Drive-Thru"}
]

for branch in bankOfAmerica:
    address = branch["address"]
    phone = branch["phone"]
    print(f"Street: {address}, Phone Number: {phone}")

