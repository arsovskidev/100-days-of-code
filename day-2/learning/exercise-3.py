# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

print(year % 4 == 0)
print(year % 100 == 0)
print(year % 400 == 0)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year.")
        else:
            print("Not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("Not a leap year.")
