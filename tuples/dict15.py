"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

restDict = [
    {"name":"Dunkin'","location":"Dedham, MA"},
    {"name":"Red Fox","location":"Jackson, NH"},
    {"name":"Horsefeathers","location":"North Conway, NH"},
    {"name":"The Salty Pig","location":"Boston, MA"}]
print(f"The dictionary is {restDict}\n")

print('restDict and their Locations')
for c in restDict:
    print(f'{c["name"]}: {c["location"]}')
# change a value
restDict[1]["location"] = "Kendall Square, Cambridge, MA"
print('\nRestaurants and their New Locations')
for c in restDict:
    print(f'{c["name"]}: {c["location"]}')
# add a new field for everyone
for c in restDict:
    c["fee"]=50.00
print('\nRestaurants and their New Fees')
for c in restDict:
    print(f'{c["name"]}: {c["location"]}, ${c["fee"]:,.2f}')
#delete from the list
restDict.pop(0)  # bye bye Bentley
print('\nNo More Dunkin')
for c in restDict:
    print(f'{c["name"]}: {c["location"]}, ${c["fee"]:,.2f}')
# add a new dict to the list
maine = {"name":"Oxford House In","location":"Frueburg, ME", "fee":25}
restDict.insert(2, maine)
print('\nNew Dictionary of Resturants')
for c in restDict:
    print(f'{c["name"]}: {c["location"]}, ${c["fee"]:,.2f}')

# delete the tuition field for everyone
for c in restDict:
    del (c["fee"])
print('\nNo More Fee')
for c in restDict:
    print(f'{c["name"]}: {c["location"]}')
