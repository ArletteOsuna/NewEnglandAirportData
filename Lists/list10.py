"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
alist = ['accounting','finance']
print(f"The original list is {alist}")
alist.append("marketing")
print(f"\nThe new list is {alist}")

alist = ['accounting','finance']
blist = ['economics','management']
alist.extend(blist)
print(f"The new list is {alist}")

alist = ['accounting','finance']
alist.insert(1,'economics')
print(f"The new list is {alist}")
alist.insert(3,'management')
print(f"The new list is {alist}")