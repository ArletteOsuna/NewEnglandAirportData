"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
dictHotel = {"New York":[ 185, 174, 190, 200],
             "Boston": [175, 1150, 185, 300],
             "Chicago": [86, 91, 194, 200],
             "Los Angeles": [165, 151, 115, 150]}
print(f"The dictionary is {dictHotel}")

dictHotel['Dallas'] = [125, 250, 350,200]
print(f"The dictionary is {dictHotel}\n")

priceList = []
for h in dictHotel:
    price = max(dictHotel[h])
    priceList.append(price)
    print (f"The most expensive hotel in {h} costs ${price:.2f}.")

print(priceList)
hotel = []
for key in dictHotel:
    hotel.append(key)

maxPrice = max(priceList)
value = priceList.index(maxPrice)
hotelName = hotel[value]

print (f"\nThe most expensive hotel is in {hotelName} and costs ${maxPrice:.2f}.")