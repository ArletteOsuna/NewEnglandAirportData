"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
fout = open('output.txt', 'w')
line1 = "We are learning how to write\n"
fout.write(line1)
line2 = 'to text files in Python\n'
fout.write(line2)
fout.close()

fhand = open('output.txt')
print("Output of Write function is ")
for line in fhand:
    line = line.rstrip()
    print(line)

# Program to show various ways to read and
# write data in a file.
fout = open("output.txt", "w")
line = "We are learning how to write\n"+"to text files in Python\n"
fout.writelines(line)
fout.close()       #to change file access modes


