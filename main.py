import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_colour = data["Primary Fur Color"].value_counts()

primary_fur_colour_data = pd.DataFrame(primary_fur_colour)
primary_fur_colour_data.to_csv("squirrel_count.csv")