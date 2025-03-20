import turtle as t
import random as r


s=t.Screen()
s.setup(width=500,height=400)
colors = ['red','green','blue','yellow','purple','orange']
y_positions = [-80,-40,-0,40,80,120]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

bet = s.textinput(title='Who will win the race',prompt='Enter the color of the turtle you think would win.').lower()

if bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 220 :
            is_race_on = False
            winning_color = turtle.pencolor()
            
            if bet == winning_color:
                print(f"You Won ! Your turtle with {bet} has won the race.") 
            else:
                print(f"You Lost ! Your turtle with {bet} has lost the race.") 
            
        r_dist = r.randint(0,10)
        turtle.forward(r_dist)


s.screensize()
s.exitonclick()
