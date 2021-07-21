print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("Child tickets costs $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets costs $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0
    else:
        print("Adult tickets costs $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken? yes/no. ")

    if wants_photo == "yes":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
