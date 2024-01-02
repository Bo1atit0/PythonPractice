"""

"""
weight = input("Enter Your Weight (KG): ")
height = input("Enter Your Height (m^2): ")

bmi = float(weight) / float(height)

if bmi < 18.5:
    print("Your BMI is {}".format(bmi))
    print("You are Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Your BMI is {}".format(bmi))
    print("You are Normal Weight")
elif bmi >= 25.0 and bmi <= 29.9:
    print("Your BMI is {}".format(bmi))
    print("You are Overweight(Pre-Obese)")
elif bmi >= 30.0 and bmi <= 34.9:
    print("Your BMI is {}".format(bmi))
    print("You are Obese(Class 1)")
elif bmi >= 35.0 and bmi <= 39.9:
    print("Your BMI is {}".format(bmi))
    print("You are Clinically Obese(Class 2)")