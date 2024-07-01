import turtle as t
import random

timmy = t.Turtle()

t.colormode(255)
screen = t.Screen()

screen_size = (400, 300)

colors = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81)]

timmy.speed("slow")

def draw_dot():
    for _ in range(10):
        timmy.pendown()
        timmy.dot(40, random.choice(colors))
        timmy.penup()
        timmy.forward(70)

def move_left():
    timmy.penup()
    timmy.right(90)
    timmy.forward(70)
    timmy.right(90)
    timmy.forward(70)

def move_right():
    timmy.penup()
    timmy.left(90)
    timmy.forward(70)
    timmy.left(90)
    timmy.forward(70)


def move_sequence():
    draw_dot()
    move_left()
    draw_dot()
    move_right()


def move():
    timmy.penup()
    timmy.setx(-325)
    timmy.sety(300)
    move_sequence()
    move_sequence()
    move_sequence()
    move_sequence()
    draw_dot()
    move_left()
    draw_dot()

move()
screen.exitonclick()
