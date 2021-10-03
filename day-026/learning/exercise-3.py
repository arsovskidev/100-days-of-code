import os

list_1 = []
list_2 = []

with open(os.path.dirname(os.path.abspath(__file__)) + "/file1.txt", "r") as file:
    list_1 = file.readlines()

with open(os.path.dirname(os.path.abspath(__file__)) + "/file2.txt", "r") as file:
    list_2 = file.readlines()

result = [int(number) for number in list_1 if number in list_2]

# Write your code above 👆

print(result)
