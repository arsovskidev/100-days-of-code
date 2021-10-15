# File Not Found
# with open("a_file.txt") as file:
#     file.read()

# Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# Index Error
# fruit_list = ["Apple", "Banana"]
# fruit = fruit_list[5]

# Type Error
# text = "abc"
# print(text + 5)

# try:
#     file = open("day-030/learning/a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("day-030/learning/a_file.txt", "w")
#     file.write("Something")
# except KeyError as message:
#     print(f"The key {message} does not exist.")
# else:
#     print("Success without errors!")
# finally:
#     raise TypeError("This is an error that I made up.")
#     # file.close()
#     # print("Successfully executed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("The height can't be more than 3 meters.")
bmi = weight / height ** 2
print(bmi)
