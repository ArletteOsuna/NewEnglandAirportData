"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
fhand = open('poem.txt', 'r+')
lines = fhand.read()
fhand.write(lines)
fhand.close()

print("Demonstration of Simultaneous Read and Write")
fhand = open("poem.txt", "r")
for line in fhand:
    line = line.rstrip()
    print(line)