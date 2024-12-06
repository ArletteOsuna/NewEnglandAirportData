"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

fhand_in = open("poem.txt")
fhand_out = open("poem2.txt","w")
i = 1
print("The Zen of Python")
for line in fhand_in:
    print(line.rstrip())
    fhand_out.write(str(i) + ": " + line)
    i = i + 1
fhand_in.close()
fhand_out.close()

print("\nThe Zen of Python with Line Numbers")
fhand = open("poem2.txt","r")
for line in fhand:
    line=line.rstrip()
    print(line)
fhand.close()