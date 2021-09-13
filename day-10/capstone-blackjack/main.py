############### Blackjack Project #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(list):
    if len(list) == 2 and sum(list) == 21:
        return 1

    if sum(list) > 21 and 11 in list:
        list.remove(11)
        list.append(1)

    return sum(list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 1:
        return "Lose, computer has a Blackjack!"
    elif user_score == 1:
        return "Win, you have a Blackjack!"
    elif user_score > 21:
        return "You went over 21, you lose..."
    elif computer_score > 21:
        return "Win, computer went over 21!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def main():
    print(logo)

    user_cards = []
    computer_cards = []
    user_finished = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not user_finished:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 1 or computer_score == 1 or user_score > 21:
            user_finished = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_cards.append(deal_card())
            else:
                user_finished = True

    while computer_score != 1 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards are: {user_cards}, score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, score: {computer_score}")
    print(compare(user_score, computer_score))


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_terminal()
    main()
