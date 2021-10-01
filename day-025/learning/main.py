# import os
# import csv

# temperatures = []
# with open(
#     os.path.dirname(os.path.abspath(__file__)) + "/weather_data.csv", mode="r"
# ) as file:
#     data = csv.DictReader(file)
#     for row in data:
#         temperatures.append(int(row["temp"]))

# print(temperatures)

import os
import pandas

# data = pandas.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(f"min-temp: {data['temp'].min()}")
# print(f"avg-temp: {data['temp'].mean()}")
# print(f"max-temp: {data['temp'].max()}")

# print(data[data.temp == data["temp"].max])

# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# monday = data[data["day"] == "Monday"]

# monday_temp_fahrenheit = (monday["temp"] * 1.8) + 32
# print(monday_temp_fahrenheit)

# Create a dataframe from scratch.

# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
# data = pandas.DataFrame(data_dict)
# data.to_csv(os.path.dirname(os.path.abspath(__file__)) + "/new_data.csv")

colors = ["Gray", "Cinnamon", "Black"]
count = []

data = pandas.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/squirrel.csv")

gray = data[data["Primary Fur Color"] == colors[0]]
count.append(len(gray.index))
cinnamon = data[data["Primary Fur Color"] == colors[1]]
count.append(len(cinnamon.index))
black = data[data["Primary Fur Color"] == colors[2]]
count.append(len(black.index))

data_dict = {"colors": colors, "count": count}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv(os.path.dirname(os.path.abspath(__file__)) + "/fur_colors.csv")
