import os
from game_data import data
from art import art_logo, art_vs
import random

score = 0
game_ower = False
temp_data = {}


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


print(art_logo)

while not game_ower:
    rand_numbers = random.sample(range(0, 49), 2)

    if temp_data:
        a = temp_data
    else:
        a = data[rand_numbers[0]]

    b = data[rand_numbers[1]]
    temp_data = b

    print(
        f"Compare A: {a.get('name')}, a {a.get('description')}, from {a.get('country')}."
    )
    print(art_vs)
    print(
        f"Against B: {b.get('name')}, a {b.get('description')}, from {b.get('country')}."
    )

    selector = input("Who has more followers? Type 'A' or 'B': ")

    if selector == "A" and a.get("follower_count") > b.get("follower_count"):
        score += 1
        clear_terminal()
        print(art_logo)
    elif selector == "B" and b.get("follower_count") > a.get("follower_count"):
        score += 1
        clear_terminal()
        print(art_logo)
    else:
        clear_terminal()
        print(art_logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        exit()
