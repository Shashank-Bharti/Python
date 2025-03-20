# from turtle import Turtle , Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# for i in range (0,8):
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.forward(100)
#     timmy.right(45)
#     my_scrn = Screen()

# print(my_scrn.canvheight)
# my_scrn.exitonclick

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"]), 
table.add_column("Type",["Electric", "Water", "Fire"])
table.align()

print(table)
