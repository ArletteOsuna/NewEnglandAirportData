# Variables for cost of an item and number of items
number = 125
cost = 2.50

# Calculate the price, tax, and total
price = cost * number
print(type(price))
tax = price * .05
total = price + tax

# Display the output
print("The total price is", total)
