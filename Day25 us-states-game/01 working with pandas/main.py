# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

#  it is quite harder to deal with above data


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)


import pandas as pd

data = pd.read_csv("weather_data.csv")

print(data['temp'])