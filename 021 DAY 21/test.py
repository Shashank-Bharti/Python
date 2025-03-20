import turtle

t = turtle.Turtle()
s = turtle.Screen()


s.listen()


def up():
    t.setheading(t.heading() + 90)
    


s.onkey(up,"Up")

is_game_on = True

while is_game_on :
    t.forward(5)
    
s.screensize()
s.exitonclick