"""
Program that finds out how many days, weeks
and months we have left if we live until 90
years old
"""


days = 365 * 90
weeks = 52 * 90
months = 12 * 90

age = int(input("How old are you? "))
if age <= 0:
    print("Enter a valid age")
elif age > 90:
    print("You have outlived this program")
else:
    age_in_days = 365 * age
    age_in_weeks = 52 * age
    age_in_months = 12 * age

    days_left = days - age_in_days
    weeks_left = weeks - age_in_weeks
    months_left = months - age_in_months

    print("You have {} days, {} weeks and {} months left".format(days_left, weeks_left, months_left))
