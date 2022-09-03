import turtle
import math


screen = turtle.Screen()
screen.bgcolor("skyblue")


george = turtle.Turtle()
george.color("black")
george.shape("turtle")


def drawRectangle(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.end_fill()


def drawTriangle(t, length, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(length)
  t.left(135)
  t.forward(length / math.sqrt(2))
  t.left(90)
  t.forward(length / math.sqrt(2))
  t.left(135)
  t.end_fill()


def drawParallelogram(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.left(30)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(120)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(90)
  t.end_fill()

george.penup()
george.goto(-150, -120)
george.pendown()
drawRectangle(george, 100, 110, "blue")

george.penup()
george.goto(-120, -120)
george.pendown()
drawRectangle(george, 40, 60, "lightgreen")

george.penup()
george.goto(-150, -10)
george.pendown()
drawTriangle(george, 100, "magenta")

george.penup()
george.goto(-50, -120)
george.pendown()
drawParallelogram(george, 60, 110, "yellow")

george.penup()
george.goto(-30, -60)
george.pendown()
drawParallelogram(george, 20, 30, "brown")

george.penup()
george.goto(-50, -10)
george.pendown()
george.fillcolor("orange")
george.begin_fill()
george.left(30)
george.forward(60)
george.left(105)
george.forward(100 / math.sqrt(2))
george.left(75)
george.forward(60)
george.left(105)
george.forward(100 / math.sqrt(2))
george.left(45)
george.end_fill()
turtle.done()