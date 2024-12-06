"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Assignment 3:
This program calculates the total cost of owning and commuting with an electric vehicle (EV).
It allows users to customize their vehicle selection, calculate monthly leasing or purchase payments,
 and estimate commuting costs including fuel, parking, and time spent. The output provides a comprehensive
 breakdown of both vehicle and commuting expenses.)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
# Constants
TAX_RATE = 0.0625
TOW_HITCH_PRICE = 8000
FEDERAL_TAX_CREDIT = 7500
DOWN_PAYMENT = 3000
LEASE_RATE = 0.015

months = 0
car_price = 0
federal_tax = 0
total_payment = 0
balance_leasing = 0
income = 0

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

# Determine if leasing
leasing = input('Do you want the leasing option? ([Y], [N]): ').lower()

# If leasing, ask for months

if leasing == "n":
    federal_tax = input("Do you want to apply for the Federal Tax Credit? ([Y], [N]): ").lower()
    if federal_tax == 'y':
        income = input("Is your annual income less than $150,000? ([Y], [N]): ").lower()
        if income == 'y':
            print('\nFederal Tax Credit has been applied to your order.')
            print()
        car_price -= FEDERAL_TAX_CREDIT  # Deduct tax credit
else:
    months = int(input('Please enter the leasing months between 1 and 9: '))
    if months < 1 or months > 9:
        print("Invalid number of months. Setting to 9.")
        months = 9
'''
# Federal Tax Credit Option
federal_tax = 0
if leasing == "n":
    federal_tax = input("Do you want to apply for the Federal Tax Credit? ([Y], [N]): ").lower()
    if federal_tax == 'y':
        income = input("Is your annual income less than $150,000?")
        if income == 'y':
            print('\nFederal Tax Credit has been applied to your order.')
            print()
        car_price -= FEDERAL_TAX_CREDIT  # Deduct tax credit
'''
# Adding Tow Hitch
if hitch == 'y':
    car_price += TOW_HITCH_PRICE

# Calculate Monthly Payment and Tax
monthly_payment = 0.015 * car_price
monthly_tax = monthly_payment * TAX_RATE
total_payment = (monthly_payment * months) + (monthly_tax * months)

# Output Summary
print(f"\n{'Order Summary ':=^43}")
print(f'{"Model:":20s}{model.upper()}')

# Map wheel drive input to full descriptions
wheel_drive_map = {'f': 'Front-Wheel Drive', 'r': 'Rear-Wheel Drive', 'a': 'All-Wheel Drive'}
wheel_full = wheel_drive_map.get(wheel, 'Unknown Drive')  # Default to 'Unknown Drive' if something goes wrong
print(f'{"Wheel Drive:":20s}{wheel_full}')

# Map color input to full color names
color_map = {'w': 'WHITE', 'b': 'BLUE', 'r': 'RED'}
color_full = color_map.get(color)
print(f'{"Color:":20s}{color_full}')
if income == 'y':
    print(f'{"Payment:":20s}Cash')
    print('\n* Applied the $7,500 Federal Tax Credit')

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
if leasing == 'y':
    print("\nMonth\tMonthlyPmt\tMonthlyTax\tTotalPmt\tBalance")

# total = total_payment
for month in range(1, months + 1):
    total_payment = monthly_payment + monthly_tax + total_payment
    # balance_leasing = total - total_payment
    balance = car_price - DOWN_PAYMENT
    print(f"{month:>3}\t\t${monthly_payment:>8,.2f}\t${monthly_tax:>1,.2f}\t\t${total_payment:>4,.2f}\t\t${balance_leasing:>4,.2f}")
