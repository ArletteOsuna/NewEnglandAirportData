"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
TAX_RATE = 0.0625
TOW_HITCH_PRICE = 8000
FEDERAL_TAX_CREDIT = 7500
DOWN_PAYMENT = 3000
LEASE_RATE = 0.015
monthly_payment = 0
total_lease_payment = 0
federal_tax = 0
annual_income = 0

print(f"{' Build Your EV ':=^43}")
model = input('Please select the EV model (Sedan, SUV): ').lower()
while model != 'sedan' and model != 'suv':
    print("Invalid model")
    model = input('Please select the EV model (Sedan, SUV): ').lower()
hitch = 'n'
if model == 'suv':
    hitch = input('Do you want to add the tow hitch? ([Y], [N]): ').lower()
wheel = input('Please select the wheel drive type (Front [F], Rear [R], All [A]): ').lower()
color = input('Please select the color (White [W], Blue [B], Red [R]): ').lower()
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

# Determine the price for the SUV
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

leasing = input('Do you want the leasing option? ([Y], [N]): ')

if leasing == "n":
    federalTax = input("Do you want to apply for the Federal Tax Credit? ([Y], [N]): ")
    if federalTax == "Y":
        annual = input("Is your annual income less than $150,000? [Y], [N]: ")
        if annual == "Y":
            print("Federal Tax Credit has been applied to your order.")
else:
    months = int(input('Please enter the leasing months between 1 and 9: '))
    if months < 1 or months > 9:
        print("Invalid number")
        months = int(input('Please enter the leasing months: '))
if model == 'sedan':
    car_price = 'sedan'[wheel][color]
else:
    car_price = 'suv'[wheel][color]
    if hitch == 'y':
        car_price += TOW_HITCH_PRICE

if leasing == 'n' and federal_tax == 'y' and annual_income == 'y':
    car_price -= FEDERAL_TAX_CREDIT

print(f"{'Order Summary ':=^43}")
print(f'{'Model:':20s}{model}')

print(f'{'Wheel:':20s}{wheel}-Wheel Drive')
if wheel == 'f':
    print('Front')
elif wheel == 'r':
    print('Rear')
elif wheel == 'a':
    print('All')
print(f'{'Color:':20s}{color}')
if color == 'w':
    print('WHITE')
if color == 'b':
    print('BLUE')
if color == 'r':
    print('RED')

if model == 'suv' and hitch == 'y':
    print('*Added the Tow Hitch')
if leasing == 'n':
    subtotal = car_price
    tax = subtotal * TAX_RATE
    total = subtotal + tax
    print(f'{'Subtotal':20s}{subtotal:.2f}')
    print(f'{'Tax':20s}{tax:.2f}')
    print(f'{"-" * 43}')
    print(f'{'Total':20s}{total:.2f}')
else:
    down_payment = DOWN_PAYMENT
    monthly_payment = car_price * LEASE_RATE
    monthly_tax = monthly_payment * TAX_RATE
    total_lease_payment = down_payment + (monthly_payment * months) + (monthly_tax * months)
print(f'{'Car Price:':20s}{car_price:,.2f}')
print(f'{'Payment:':20s}{leasing}')
print(f'{'Months:':20s}{months}')
print(f'{'Monthly Payment:':20s}{monthly_payment:,.2f}')
print(f'{'Monthly Tax:':20s}{tax:,.2f}')
print(f'{"-" * 43}')
print(f'{'Total:':20s}{total_lease_payment:,.2f}')

