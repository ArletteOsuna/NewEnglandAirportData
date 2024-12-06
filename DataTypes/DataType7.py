# Variables for cost of an item and number of items
name = input("Enter your name: ")
number = int(input("Enter the number of items you would like: "))
cost = float(input("Enter the cost of item you would like: "))

# Calculate the price, tax and total
price = cost * number
tax = price * .05
total = price + tax

# Display the output
print("The total price is", total)
print("The total price", round(total, 2))
print("The total price is $", round(total, 2))
print("The total price is $" + str(round(total, 2)))