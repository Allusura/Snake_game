from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
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
        # Starting position of the snake (3 squares)
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # Get the position of the last "square" of the snake, and move the "square" to the position of the square
        # in-front of it, essentially making a chain of "squares"
        for seg_num in range(len(self.segments) - 1, 0, -1, ):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # Functions to control movement, disallowing it to go back on itself.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            pass
