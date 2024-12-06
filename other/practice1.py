"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
# Constants
TAX_RATE = 0.0625
TOW_HITCH_PRICE = 8000
FEDERAL_TAX_CREDIT = 7500
DOWN_PAYMENT = 3000
LEASE_RATE = 0.015

# User Inputs
print(f"{'Build Your EV':=^43}")
model = input('Please select the EV model (Sedan, SUV): ').lower()
while model != 'sedan' and model != 'suv':
    print("Invalid model")
    model = input('Please select the EV model (Sedan, SUV): ').lower()
hitch = 'n'
if model == 'suv':
    hitch = input('Do you want to add the tow hitch? ([Y], [N]): ').lower()
wheel = input('Please select the wheel drive type (Front [F], Rear [R], All [A]): ').lower()

color = input('Please select the color (White [W], Blue [B], Red [R]): ').lower()

# Determine the car price based on user selections
car_price = 0
if model == 'sedan':
    if wheel == 'f':
        if color == 'w':
            car_price = 24000
        elif color == 'b':
            car_price = 24500
        elif color == 'r':
            car_price = 25000
    elif wheel == 'r':
        if color == 'w':
            car_price = 26000
        elif color == 'b':
            car_price = 26500
        elif color == 'r':
            car_price = 27000
    elif wheel == 'a':
        if color == 'w':
            car_price = 28000
        elif color == 'b':
            car_price = 28500
        elif color == 'r':
            car_price = 29000

elif model == 'suv':
    if wheel == 'f':
        if color == 'w':
            car_price = 26000
        elif color == 'b':
            car_price = 26500
        elif color == 'r':
            car_price = 27000
    elif wheel == 'r':
        if color == 'w':
            car_price = 28000
        elif color == 'b':
            car_price = 28500
        elif color == 'r':
            car_price = 29000
    elif wheel == 'a':
        if color == 'w':
            car_price = 30000
        elif color == 'b':
            car_price = 30500
        elif color == 'r':
            car_price = 31000

leasing = input('Do you want the leasing option? ([Y], [N]): ').lower()

# Processing Leasing Option
months = 0
if leasing == "n":
    federal_tax = input("Do you want to apply for the Federal Tax Credit? ([Y], [N]): ").lower()
else:
    months = int(input('Please enter the leasing months between 1 and 9: '))
    if months < 1 or months > 9:
        print("Invalid number of months. Setting to 9.")
        months = 9

# Adding Tow Hitch
if hitch == 'y':
    car_price += TOW_HITCH_PRICE

# Calculate Monthly Payment and Tax
monthly_payment = 1.5/100 * car_price
monthly_tax = monthly_payment * TAX_RATE
total_payment = (monthly_payment * months) + (monthly_tax * months)

# Output Summary
print(f"\n{'Order Summary ':=^43}")
print(f'{"Model:":20s}{model.upper()}')
print(f'{"Wheel Drive:":20s}{wheel.upper()}-Wheel Drive')
if wheel == 'f':
    print('Front')
elif wheel == 'r':
    print('Rear')
elif wheel == 'a':
    print('All')
print(f'{"Color:":20s}{color.upper()}')

if model == 'suv' and hitch == 'y':
    print('\n*Added the Tow Hitch')

print(f'{"\nCar Price:":20s}${car_price:,.2f}')
print(f'{"Payment:":20s}Leasing')
print(f'{"Months:":20s}{months}')
print(f'{"Monthly Payment:":20s}${monthly_payment:,.2f}')
print(f'{"Monthly Tax:":20s}${monthly_tax:,.2f}')
print(f'{"-" * 43}')
print(f'{"Total:":20s}${total_payment:,.2f}')

# Breakdown of Payments
print("\nMonth\tMonthlyPmt\tMonthlyTax\tTotalPmt\tBalance")
balance = car_price - DOWN_PAYMENT
# fix this, didnt learn

total = total_payment
total_payment = 0
balance_leasing = 0
for month in range(1, months + 1):
    total_payment = monthly_payment + monthly_tax + total_payment
    balance_leasing = total - total_payment
    print(f"{month:>5}\t${monthly_payment:>9,.2f}\t\t${monthly_tax:>5,.2f}\t\t${total_payment:>5,.2f}\t\t${balance_leasing:>5,.2f}")

