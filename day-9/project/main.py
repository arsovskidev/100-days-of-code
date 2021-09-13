from os import system, name
from art import logo


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def find_winner(bidders):
    winner_name = ""
    winner_bid = 0

    for bidder in bidders:
        if bidders[bidder] > winner_bid:
            winner_name = bidder
            winner_bid = bidders[bidder]

    print(f"Winner is {winner_name} with a bid of ${winner_bid}")


print(logo)

bidders = {}
running = True

while running:
    name = input("What is your name? ")
    bid = int(input("How much will you bid? $"))

    bidders[name] = bid

    status = input("Are there any other users wo want to bid? 'yes' or 'no'\n")

    if status == "no":
        clear()
        running = False
        find_winner(bidders)
    else:
        clear()
