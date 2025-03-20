import turtle


t = turtle.Turtle()
s = turtle.Screen()


def move_forward():
    t.forward(5)
    
def move_backward():
    t.backward(5)
    
def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)
    
    
def clear_screen():
    t.reset()
    
turtle.listen()

turtle.onkey(clear_screen, "c")
turtle.onkey(turn_left, "Left")
turtle.onkey(move_forward , "Up")
turtle.onkey(turn_right, "Right")
turtle.onkey(move_backward, "Down")

s.screensize()
s.exitonclick()