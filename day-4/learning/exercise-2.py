# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

import random

number_of_names = len(names)
random = random.randint(0, number_of_names - 1)

result = names[random]
# result = random.choice(names)

print(f"{result} is going to buy the meal today!")
