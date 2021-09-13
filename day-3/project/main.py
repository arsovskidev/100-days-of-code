print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right"\n'
).lower()

if choice != "left":
    print("You fell into a hole, Game Over.")
    exit()

choice = input(
    'You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
).lower()

if choice != "wait":
    print("You got attacked by trout and died, Game Over.")
    exit()

choice = input(
    "You arrive at the island unharmed. There is a table with 3 buttons. One red, one yellow and one blue. Which button will you press?\n"
).lower()

if choice == "yellow":
    print("You Win!")
    exit()
elif choice == "red":
    print("You started fire and died by burning, Game Over.")
    exit()
elif choice == "blue":
    print("Tiger was released and attacked you, Game Over.")
    exit()
else:
    print("Game Over.")
    exit()
