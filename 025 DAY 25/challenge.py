import pandas

data = pandas.read_csv("weather_data.csv")

temp_celsius = data[data.day =='Monday'].temp[0]

temp_fahrenheit = (temp_celsius * (9/5)) + 32

print(temp_fahrenheit)
