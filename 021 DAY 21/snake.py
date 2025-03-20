import turtle as t


BODY_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for pos in BODY_POS :
            self.add_segment(pos)
            
    def add_segment(self,pos):
            new_seg = t.Turtle(shape='square')
            new_seg.penup()
            new_seg.color('white')
            new_seg.goto(pos)
            self.segments.append(new_seg)
    def extend(self):
        self.add_segment(self.segments[-1].position())            
    
    def move(self):
        
         for seg_num in range(len(self.segments) - 1 ,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # print(f"{new_x}, {new_y}")
            self.segments[seg_num].goto(new_x,new_y)    
        
         self.head.forward(MOVE_DIST)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def lt(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def rt(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def dn(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
