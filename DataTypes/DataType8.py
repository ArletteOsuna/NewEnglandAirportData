# Variables for cost of an item and number of items
SALES_TAX = .05
number = int(input("Enter the number of items you would like: "))
cost = float(input("Enter the cost of item you would like: "))

# Calculate the price, tax and total
price = cost * number
tax = price * SALES_TAX
total = price + tax

# Display the output
print("The total price is", total)