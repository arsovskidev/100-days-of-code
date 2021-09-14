################### Scope ####################

# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope


# def drink_potion():
#     potion_strength = 10
#     print(potion_strength)


# drink_potion()

# # Global Scope
# player_health = 100


# def drink_potion():
#     potion_strength = 10
#     print(player_health)


# drink_potion()

# # There is no Block Scope
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# # Modifying Global Scope

# enemies = 1


# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1


# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
URL = "https://www.astennu.com"


def calc():
    PI
