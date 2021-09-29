import os

# file = open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt")
# contents = file.read()
# file.close()
# print(contents)

# with open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt") as file:
#     contents = file.read()
#     print(contents)

with open(os.path.dirname(os.path.abspath(__file__)) + "/data.txt", mode="a") as file:
    file.write("Hello World.\n")
