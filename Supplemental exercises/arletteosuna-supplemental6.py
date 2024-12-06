"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

print('Exercise #1:')
# The purpose of this program is to count the number of words in a file.
file_name = input("Enter file name: ")

try:
    # Open file in read mode
    with open(file_name, 'r') as file:
        # Read the content and split into words
        words = file.read().split()
        # Count the words
        word_count = len(words)

    # Display the result
    print(f'Number of words in {file_name} is {word_count}')

except FileNotFoundError:
    print(f"File {file_name} not found.")

print('\nExercise #2:')
# The purpose of this program is to extract and save all five-letter words from a file.
import re

# Input and output filenames
input_file_name = 'Alice.txt'
output_file_name = 'FiveLetterWords.txt'

try:
    # Open input file in read mode and output file in write mode
    with open(input_file_name, 'r') as file, open(output_file_name, 'w') as output_file:
        for line in file:
            # Find words that are exactly five letters long, including punctuation
            words = re.findall(r'\b\w{5}\b', line)
            # Write each five-letter word to the output file, one per line
            for word in words:
                output_file.write(word + '\n')

    # Notify user of success
    print(f"File {output_file_name} has been written")

except FileNotFoundError:
    print(f"File {input_file_name} not found.")

print('\nExercise #3:')
# The purpose of this program is to extract and display numbers from a file.
file_name = input("Enter file name: ")

try:
    # Open file in read mode
    with open(file_name, 'r') as file:
        print(f"The numbers in file {file_name} are:")
        for line in file:
            # Find all numbers in the line
            numbers = re.findall(r'\d', line)
            for number in numbers:
                # Print each number found
                print(number)

except FileNotFoundError:
    print(f"File {file_name} not found.")

print('\nExercise #4:')
# The purpose of this program is to find and display the longest words in a file. A key feature is word.strip.
file_name = 'alice.txt'

try:
    # Open file in read mode
    with open(file_name, 'r') as file:
        longest_words = []
        max_length = 0
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('.,!?;:"()[]{}')  # Remove external punctuation
                if len(word) > max_length:
                    longest_words = [word]
                    max_length = len(word)
                elif len(word) == max_length:
                    longest_words.append(word)

    # Display the longest words
    print(f'The longest words in the file "{file_name}" are {", ".join(longest_words)}')

except FileNotFoundError:
    print(f"File {file_name} not found.")