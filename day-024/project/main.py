import os

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PLACEHOLDER = "[name]"

with open(DIRECTORY + "/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

with open(DIRECTORY + "/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()
    for name in names:
        stripped_name = name.strip()
        with open(
            DIRECTORY + f"/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w"
        ) as file:
            new_letter = letter.replace(PLACEHOLDER, stripped_name)
            file.write(new_letter)
