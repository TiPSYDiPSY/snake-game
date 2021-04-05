from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(x=new_x, y=new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake_body.append(new_turtle)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def reset(self):
        for seg in self.snake_body:
            seg.hideturtle()
            seg.clear()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
