import turtle
import time
import snake
import food
import scoreboard
speed = 0.2
s = turtle.Screen()
s.setup(width=600,height=600)
s.bgcolor('black')
s.title('My Snake Game')
s.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

s.listen()

s.onkey(snake.up,"Up")
s.onkey(snake.dn,"Down")
s.onkey(snake.lt,"Left")
s.onkey(snake.rt,"Right")

game_is_on = True

while game_is_on:
    s.update()
    time.sleep(speed)
    snake.move()
    
    #check if food is in the proximity of the snake head
    if snake.head.distance(food) < 15:
        speed = 0.2
        
        snake.extend()
        if food.color() == ('blue','blue') :
            speed -= 0.1
            scoreboard.booster()
        food.refresh()
        
        scoreboard.inc_score() 
        scoreboard.reset()
        
    # check for collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # check for self collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            
    
s.screensize()
s.exitonclick()
