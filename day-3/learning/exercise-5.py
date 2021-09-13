# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

combined_names = name1.lower() + name2.lower()

letter_t = combined_names.count("t")
letter_r = combined_names.count("r")
letter_u = combined_names.count("u")
letter_e = combined_names.count("e")
letter_l = combined_names.count("l")
letter_o = combined_names.count("o")
letter_v = combined_names.count("v")

total_true = str(letter_t + letter_r + letter_u + letter_e)
total_love = str(letter_l + letter_o + letter_v + letter_e)

score = int(total_true + total_love)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
