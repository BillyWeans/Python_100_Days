# import csv
#
# with open("weather_data.csv", mode="r") as f_weather_data:
#     data = csv.reader(f_weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
sq_black = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
sq_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
sq_gray = sq_black = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()

print(sq_black)

df = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [sq_black, sq_cinnamon, sq_gray],
}

sq_fur_colors = pandas.DataFrame(data=df)

print(sq_fur_colors)

sq_fur_colors.to_csv("squirrel_counts_by_fur.csv")

