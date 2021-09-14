from math import e
import random

logo = """
  _   _                    _                    _____                                    
 | \ | |                  | |                  / ____|                                   
 |  \| | _   _  _ __ ___  | |__    ___  _ __  | |  __  _   _   ___  ___  ___   ___  _ __ 
 | . ` || | | || '_ ` _ \ | '_ \  / _ \| '__| | | |_ || | | | / _ \/ __|/ __| / _ \| '__|
 | |\  || |_| || | | | | || |_) ||  __/| |    | |__| || |_| ||  __/\__ \\__ \|  __/| |   
 |_| \_| \__,_||_| |_| |_||_.__/  \___||_|     \_____| \__,_| \___||___/|___/ \___||_|   
                                                                                         
"""


def check_number(computer_number, user_number):
    if computer_number > user_number:
        print("Too low.")
        return 0

    if computer_number < user_number:
        print("Too high.")
        return 0

    if computer_number == user_number:
        print(f"You got it! The answer was {computer_number}.")
        return 1


computer_number = random.randint(1, 100)
attempts = 0

print(logo)
print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
)

while True:
    difficulty_input = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_input == "easy":
        attempts = 10
        break
    if difficulty_input == "hard":
        attempts = 5
        break

while attempts != 0:
    print(f"You have {attempts} remaining to guess the number.")
    user_number = int(input("Make a guess: "))

    result = check_number(computer_number, user_number)
    attempts -= 1

    if result == 1:
        break
    elif result == 0:
        if attempts != 0:
            print("Guess again.")
        else:
            print("Game over!")
