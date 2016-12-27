from turtle import *

def draw_square():
    for x in range(0, 4):
        forward(100)
        right(90)

def draw(angle):
    window = Screen()
    window.setup(400, 800)
    window.bgcolor('red')

    shape('turtle')
    color('yellow')
    speed('fast')
    penup()
    setpos(0, -200)
    pendown()

    for x in range(0, 2):
        while heading() < 90:
            draw_square()
            left(angle)

        setheading(90)
        forward(100)
        left(180)

        while heading() > 180:
            draw_square()
            right(angle)
        setheading(90)
        forward(100)
        right(90)

    while heading() < 90:
        draw_square()
        left(angle)

    window.exitonclick()

draw(6)
