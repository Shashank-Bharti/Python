from turtle import Screen
import random as ran
import turtle as t
win_width, win_height, bg_color = 2000, 2000, 'black'

tim = t.Turtle()



# tim.shape("turtle")
# ---challenge 1---
'''for i in range (4):
tim.forward(100)
tim.left(90)'''


# ---challenge 2----
'''for i in range (20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
'''



# ---challenge 3----
'''colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat", "SlateGray","SeaGreen"]

def drawshape(sides):
    5 = 360 / sides 
    for _ in range(sides) :
        
        tim.forward(100)
        tim.right(5)


for shape_sides in range(3,11):
    tim.color(r.choice(colors))
    drawshape(shape_sides)
    '''
    

# ---challenge 4----

'''def random_walk ():
    moving_values = [0,50]
    turning_values = [0,90]
    actions = [
    tim.forward(r.choice(moving_values)),
    tim.backward(r.choice(moving_values)),
    tim.left(r.choice(turning_values)),
    tim.right(r.choice(turning_values)),
    ]
    r.shuffle(actions)
    
    r.choice(actions)

colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat", "SlateGray","SeaGreen"]

for _ in range (200):
    tim.hideturtle()
    tim.pensize(1)
    tim.shape("circle")
    tim.color(r.choice(colors))
    tim.speed('fastest')
    random_walk()
'''
# ======Solution=====

'''colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat", "SlateGray","SeaGreen"]

directions = [0,90,180,270]


for _ in range (200):
    tim.hideturtle()
    tim.pensize(10)
    tim.color(r.choice(colors))
    tim.speed('fastest')
    tim.forward(30)
    tim.setheading(r.choice(directions))
'''



# ---Challenge 4.5----

'''t.colormode(255)

def random_color():
    r = ran.randint(0,255)
    g = ran.randint(0,255)
    b = ran.randint(0,255)
    
    return (r, g, b)


directions = [0,90,180,270]
tim.pensize(15)
tim.speed('fastest')

for _ in range (200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(ran.choice(directions))'''
    
# ---challenge 5----
t.colormode(255)
def random_color():
    r = ran.randint(0,255)
    g = ran.randint(0,255)
    b = ran.randint(0,255)
    
    return (r, g, b)

def circle():
    for i in range(int(360/5)):
        tim.pensize(2)
        tim.speed('fastest')
        tim.color(random_color())
        tim.circle(200)
        tim.setheading(tim.heading() + 5)
        
circle()

    
    
screen = Screen()
screen.screensize(win_width, win_height)
screen.exitonclick()