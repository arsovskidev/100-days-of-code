# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = float(height)
weight = int(weight)

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    status = "underweight"
elif bmi < 25:
    status = "normal weight"
elif bmi < 30:
    status = "overweight"
elif bmi < 35:
    status = "obese"
else:
    status = "clinically obese"

print(f"Your BMI is {bmi} and you are {status}.")
