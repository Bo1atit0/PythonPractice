"""
BMI Calculator Program

This program calculates Body Mass Index (BMI) based on user input for weight and height. It then categorizes the BMI into different weight status levels according to commonly used standards.

Usage:
1. Run the program.
2. Input your weight in kilograms when prompted.
3. Input your height in square meters when prompted.
4. The program calculates the BMI and provides a weight status level.

Note: BMI is calculated as weight (in kg) divided by the
square of height (in meters).

"""

# Get input for weight and height from the user
weight = input("Enter Your Weight (KG): ")
height = input("Enter Your Height (m): ")

# Calculate BMI
bmi = float(weight) / float(height)

# Categorize BMI into different weight status levels
if bmi < 18.5:
    print("Your BMI is {:.2f}".format(bmi))
    print("You are Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Your BMI is {:.2f}".format(bmi))
    print("You are Normal Weight")
elif 25.0 <= bmi <= 29.9:
    print("Your BMI is {:.2f}".format(bmi))
    print("You are Overweight (Pre-Obese)")
elif 30.0 <= bmi <= 34.9:
    print("Your BMI is {:.2f}".format(bmi))
    print("You are Obese (Class 1)")
elif 35.0 <= bmi <= 39.9:
    print("Your BMI is {:.2f}".format(bmi))
    print("You are Clinically Obese (Class 2)")
