"""Class: CS230--Section 1 
Name: Arlette Osuna
Date: 18 September 2024
Description: Homework 1 - This exercise calculates the monthly and annual cost of commuting
based on user input for round-trip distance, number of commuting days, and parking costs.
It also computes the time spent commuting per month and converts average speed to kilometers
per minute for additional analysis.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

cost_per_mile = 0.72  # AAA's estimate
average_speed = 45  # miles per hour
km_per = 1.609344  # miles to kilometers

print("========== Input Commuting Values ==========")
daily_round_trip = float(input("What is your daily round trip to school/work? "))
days_per_month = int(input("How many days per month do you commute? "))
parking_cost = float(input("How much do you pay for parking per month? "))

monthly_miles = daily_round_trip * days_per_month
monthly_cost = (monthly_miles * cost_per_mile) + parking_cost
annual_cost = monthly_cost * 12

# Calculations of time spent commuting per month in hours and minutes
hours_per_month = monthly_miles / average_speed
total_minutes = hours_per_month * 60
hours = int(total_minutes // 60)
minutes = total_minutes % 60

# Av speed in km per minute
avg_km_per = (average_speed * km_per) / 60

print("\n========== Commuting Statistics ==========")
print("At an average speed of", average_speed, "miles per hour,")
print("you spend", hours, "hours and", round(minutes, 2), "minutes a month commuting")
print("The average speed of", average_speed, "miles per hour is", round(avg_km_per, 2), "kilometers per minute")
print("Your estimated monthly cost of commuting is $", round(monthly_cost, 1))
print("Your estimated yearly cost of commuting is $", round(annual_cost, 1))
