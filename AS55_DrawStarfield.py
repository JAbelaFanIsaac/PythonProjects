import turtle
import random
def draw_star():
        turtle.penup()
        x=random.randint(-500,500)
        y=random.randint(-300,300)
        turtle.goto(x,y)
        turtle.bgcolor("Black")
        turtle.color("Yellow")
        sz=random.randint(0,10)
        turtle.dot(sz)
        turtle.speed(0)
for i in range(500):
    draw_star()