import pandas

data = pandas.read_csv("weather_data.csv")

# print(data['temp'])
# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data['temp'].to_list()
# print (temp_list)

# avg_temp = sum(temp_list)//len(temp_list)
# print(avg_temp)
# print(data['temp'].max())

# get data in columns 

# print(data['condition'])
# print(data.condition)

# get data in row 

# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# Create a Dataframe from Scratch

data_dict = {
    'students' : ["Amy" , "Garfield" , "Matthew" , "Jacob"],
    'scores' : [66, 45, 88, 65]
}

data = pandas.DataFrame(data_dict)

data.to_csv("scores.csv")