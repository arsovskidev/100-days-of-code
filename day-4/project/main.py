import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

input_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)

if input_choice >= 3 or input_choice < 0:
    print("You picked invalid number, you lose!")
else:
    game_images = [rock, paper, scissors]
    random_choice = random.randint(0, 2)

    print(game_images[input_choice])
    print(f"Computer chose: {game_images[random_choice]}")

    if (
        (input_choice == 0 and random_choice == 2)
        or (input_choice == 1 and random_choice == 0)
        or (input_choice == 2 and random_choice == 1)
    ):
        print("You win!")
    elif input_choice == random_choice:
        print("It's draw!")
    else:
        print("You lose.")
