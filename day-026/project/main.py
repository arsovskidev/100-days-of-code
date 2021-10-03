import os
import pandas

df = pandas.read_csv(
    os.path.dirname(os.path.abspath(__file__)) + "/nato_phonetic_alphabet.csv"
)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    user = input("Please enter a word: ").upper()
    nato = [data[letter] for letter in user]
    print(nato)
