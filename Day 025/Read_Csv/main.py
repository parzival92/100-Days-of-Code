# CSV - Tabular Data(comma seperated value)

# with open("./weather_data.csv") as csv_file:
#     data = csv_file.readlines()

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
    
# Pandas - Data Analysis Library
 
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].tolist()
# Print mean or average
avg = data["temp"].mean()
print(avg)
#Print max in a series
max = data["temp"].max()
print(max)

# Get Data in columns
print(data.condition)
print(data["condition"])

# Get data in rows
print(data[data.day == "Monday"])

#Print the row of day has the highest temperature
max_temp = data.temp.max()
print(data[data.temp == max_temp])

# Covert Monday Temperature into Fahrenheit
# Formula : (0°C × 9/5) + 32 = 32°F
print("Monday series")
mon = data[data.day == "Monday"]
print(mon)
mon_temp = mon.temp
temp_to_f = (mon_temp * 9/5) + 32
print(f"The Temperature in Fahrenheit is: {temp_to_f}")





