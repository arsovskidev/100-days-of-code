from os import system, name
import random
import art
import words


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed_letters = []

print(art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in guessed_letters:
        print("You have already tried this letter, try another one!")

    guessed_letters.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(art.stages[lives])
