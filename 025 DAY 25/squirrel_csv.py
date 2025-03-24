import pandas

data = pandas.read_csv("E:/100 Days Of Python/025 DAY 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"].unique().tolist()
color_count = data["Primary Fur Color"].value_counts().tolist()

d = {
    "Fur colors" : fur_color[1:], 
    "Color count": color_count
}

df = pandas.DataFrame(d)

df.to_csv("squirrel_count.csv")