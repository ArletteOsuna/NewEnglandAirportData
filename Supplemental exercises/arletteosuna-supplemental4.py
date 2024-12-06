"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: Supplemental Exercise 4
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

print('Exercise #1')


# The purpose of this program is to calculate the total purchase cost and tax
# amount based on item price and quantity. One key feature is the ability to apply
# a default Massachusetts sales tax rate of 6.25%.

def calculate_total_cost(num_items, item_price, sales_tax_rate=0.0625):
    purchase_price = num_items * item_price  # calculation for the price
    sales_tax_amount = round(purchase_price * sales_tax_rate, 2)
    total_cost = round(purchase_price + sales_tax_amount, 2)

    return total_cost, sales_tax_amount  # total cost & sales tax are returned


num_items = int(input('Enter the number of items: '))  # return an integer
item_price = float(input('Enter the price of each item: '))  # return a float

total_cost, sales_tax_amount = calculate_total_cost(num_items, item_price)

print(f'Your purchase price is ${total_cost} and the tax amount is ${sales_tax_amount}')

print('Exercise #2')


# The purpose of this program is to count the number of upper-case and lower-case letters
# in a string. One key feature is the ability to handle mixed case strings accurately.

def count_characters(string):
    upper_case = 0
    lower_case = 0
    # lower case and upper case loop
    for num in string:
        if num.isupper():
            upper_case += 1
        elif num.islower():
            lower_case += 1

    return upper_case, lower_case


input1 = input('Enter a string: ')
upper_case, lower_case = count_characters(input1)
print(f"No. of Upper-Case characters: {upper_case}")
print(f"No. of Upper-Case characters: {lower_case}")
# another way of doing it : print(f"No. of Upper-Case characters: {count_characters(input1)[0]}")


print('Exercise #3')


# he purpose of this program is to compute the cost of a trip based on distance,
# fuel cost, and an optional mpg value. One key feature is the use of a default
# mpg value of 50, which can be overridden by the user.

def cost_to_travel(distance, mpg, fuel_cost):
    cost = (distance / mpg) * fuel_cost  # formula for cost

    return cost


input2 = float(input('Enter distance traveled: '))
input3 = float(input('Enter cost per gallon: '))

cost = cost_to_travel(input2, 50, input3)  # mpg is given as 50
print(f'The cost to travel {input2} miles when the cost per gallon is ${input3} is ${cost}')

print('Exercise #4')


# The purpose of this program is to swap the case of each letter in a given string.
# One key feature is the ability to toggle between upper and lower case letters while
# preserving the original format of other characters.

def lower(string):
    swap = ''
    for letter in string:
        letter2 = letter.swapcase()  # loop for the letters to swap
        swap += letter2
    return swap


word = input('Enter a word: ')
print(f"The string '{word}' with the letters with swapped case is '{lower(word)}'")

print('Exercise #5')


# The purpose of this program is to calculate the “value” of a word based on a scoring
# system for vowels, consonants, and specific letters.

def calculated_value(word2):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    chars = 0
    # calculations
    for char in word2:  # loop for vowels, constants and x
        if char in vowels:
            chars += 3
        if char == 'x':
            chars += 10
        if char in consonants:
            chars += 1

    return chars


word2 = input('Enter a word: ').lower()
res = calculated_value(word2)
print(f'The value of {word2} is {res}')
