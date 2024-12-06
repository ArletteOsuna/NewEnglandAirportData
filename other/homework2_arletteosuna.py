"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Assignment 3: This program calculates the total cost of owning and commuting with an electric vehicle (EV).
The output provides a comprehensive breakdown of both vehicle and commuting expenses.)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
# Constants
SALES_TAX = 0.0625
TOW_HITCH_COST = 8000
DOWN_PAYMENT = 3000
MONTHLY_INTEREST_RATE = 0.015
FEDERAL_TAX_CREDIT = 7500
INCOME_ELIGIBILITY = 150000
SEDAN_PRICE = 24000
SUV_PRICE = 26000
WHITE = 0
BLUE = 2000
RED = 1000
REAR_SEDAN = 500
REAR_SUV = 2000
FRONT = 0
ALL = 4000

# initialize variables
price = 0
months = 0
federalTax = 0
totalPaid = 0
total_payment = 0
hitch = 'n'

print("============== Build Your EV ==============")
ev_model = input("Please select the EV model (Sedan, SUV): ").lower()
while ev_model != 'sedan' and ev_model != 'suv':
    print("Invalid model")
    ev_model = input("Please select the EV model (Sedan, SUV): ").lower()
if ev_model == 'suv':
    hitch = input("Do you want to add the tow hitch? ([Y], [N]): ").lower()

wheel_drive = input("Please select the wheel drive type (Front [F], Rear [R], All [A]): ").lower()
while wheel_drive not in 'fra':
    print("Invalid input.")
    wheel_drive = input("Please select the wheel drive type (Front [F], Rear [R], All [A]): ").lower()

color = input("Please select the color (White [W], Blue [B], Red [R]): ").lower()
while color not in 'wbr':
    print("Invalid color.")
    color = input("Please select the color (White [W], Blue [B], Red [R]): ").lower()

# add pricing for color for Sedan
if ev_model == 'sedan':
    modelString = "SEDAN"
    if color == 'r':
        price += RED
        colorString = 'RED'
    elif color == 'b':
        price += BLUE
        colorString = 'BLUE'
    else:
        price += 0
        colorString = 'WHITE'

# add pricing for type of drive for Sedan
if ev_model == 'sedan':
    price += SEDAN_PRICE
    modelString = 'SEDAN'
    if wheel_drive == 'a':
        price += ALL
        wheel_driveString = 'All'
    elif wheel_drive == 'r':
        price += REAR_SEDAN
        wheel_driveString = 'Rear'
    else:
        price += 0
        wheel_driveString = 'Front'

# add pricing for SUV color
if ev_model == 'suv':
    price += SUV_PRICE
    modelString = 'SUV'
    if color == 'r':
        price += RED
        colorString = 'RED'
    elif color == 'b':
        price += BLUE
        colorString = 'BLUE'
    else:
        price += 0
        colorString = 'WHITE'

# add pricing for SUV
if ev_model == 'suv':
    modelString = 'SUV'
    if wheel_drive == 'a':
        price += ALL
        wheel_driveString = 'All'
    elif wheel_drive == 'r':
        price += REAR_SUV
        wheel_driveString = 'Rear'
    else:
        price += 0
        wheel_driveString = 'Front'
if hitch == 'y':
    price += TOW_HITCH_COST

# leasing option
leasing = input("Do you want the leasing option? ([Y], [N]): ").lower()
if leasing == "y":
    months = int(input("Please enter the leasing months between 1 and 9: "))
    while months > 9:
        print("Invalid number.")
        months = int(input("Please enter the leasing months: "))
elif leasing == "n":
    leasing = 'Cash'
    # applied federal tax credit
    federalTax = input("Do you want to apply for the Federal Tax Credit? ([Y], [N]): ").lower()
    if federalTax == 'y':
        income = input("Is your annual income less that $150,000? ([Y], [N]): ").lower()
        if income == 'y':
            price -= FEDERAL_TAX_CREDIT
            print("\nFederal Tax Credit has been applied to your order.")

# order summary
print(f"\n{'Order Summary ':=^43}")
print(f"{"Model:":20s}{modelString}")
print(f"{"Wheel Drive:":20s}{wheel_driveString}-Wheel Drive")
print(f"{"Color:":20s}{colorString}")

if hitch == 'y':
    print("\n*Added the Tow Hitch")
if federalTax == 'y':
    tax = price * SALES_TAX
    total = price + tax
    print("\n*Applied the $7,500 Federal Tax Credit\n")
    print(f"{"Payment:":20s}{leasing}")
    print(f'{"Subtotal:":20s}${price:,.2f}')
    print(f'{"Tax:":20s}${tax:,.2f}')
    print(f'{"-" * 43}')
    print(f'{"Total:":20s}${total:,.2f}')

# if user chooses sedan
if ev_model == 'sedan' and federalTax == 'n':
    if color == 'r':
        price += 0
        print(f'{"Car Price:":20s}${price:,.2f}')
    elif color == 'b':
        price += 0
        print(f'{"Car Price:":20s}${price:,.2f}')
    else:
        price += 0
        print(f'{"Car Price:":20s}${price:,.2f}')
#  calculations
monthly_payment = 1.5/100 * price
monthly_tax = monthly_payment * SALES_TAX
total_payment = (monthly_payment * months) + (monthly_tax * months)

# if user selected leasing option
if leasing == 'y' and ev_model == 'suv':
    print(f'{"\nCar Price:":20s}${price:,.2f}')
    print(f'{"Payment:":20s}Leasing')
    print(f'{"Months:":20s}{months}')
    if hitch == 'y':
        print(f'{"Monthly Payment:":20s}${0.015 * price:,.2f}')
        print(f'{"Monthly Tax:":20s}${SALES_TAX * (0.015 * price):,.2f}')
        print(f'{"-" * 43}')
        print(f"{'Total:':20s} ${(9 * (0.015 * price)) + (9 * SALES_TAX * (0.015 * price)):,.2f}\n")
    else:  # if there is no hitch added
        print(f'{"Monthly Payment:":20s}${0.015 * price:,.2f}')
        print(f'{"Monthly Tax:":20s}${SALES_TAX * (0.015 * price):,.2f}')
        print(f'{"-" * 43}')
        print(f"{'Total:':20s} ${(9 * (0.015 * price)) + (9 * SALES_TAX * (0.015 * price)):,.2f}\n")
if ev_model == 'sedan' and federalTax == 'n':
    print(f'{"Monthly Payment:":20s}${0.015 * price:,.2f}')
    print(f'{"Monthly Tax:":20s}${SALES_TAX * (0.015 * price):,.2f}')
    print(f'{"-" * 43}')
    print(f"{'Total:':20s} ${(9 * (0.015 * price)) + (9 * SALES_TAX * (0.015 * price)):,.2f}\n")

if ev_model == 'sedan' and leasing == 'y':
    print(f'{"Car Price:":20s}${price:,.2f}')
    print(f"{"Payment:":20s}Leasing")
    print(f'{"Months:":20s}{months}')
    print(f'{"Monthly Payment:":20s}${0.015 * price:,.2f}')
    print(f'{"Monthly Tax:":20s}${SALES_TAX * (0.015 * price):,.2f}')
    print(f'{"-" * 43}')
    print(f"{'Total:':20s}${(months * (0.015*price)) + (9 * SALES_TAX * (0.015 * price)):,.2f}\n")

if leasing == 'y':
    print("Month\tMonthlyPmt\tMonthlyTax\tTotalPmt\tBalance")

balance = price - DOWN_PAYMENT

total = total_payment
total_payment = 0
balance_leasing = 0
monthly_payment = 0.015 * price
monthly_tax = SALES_TAX * monthly_payment
for month in range(1, months + 1):
    total_payment = monthly_payment + monthly_tax + total_payment
    balance_leasing = total - total_payment
    print(f"{month:>5}\t${monthly_payment:>9,.2f}\t\t${monthly_tax:>5,.2f}\t\t${total_payment:>5,.2f}\t\t${balance_leasing:>5,.2f}")
