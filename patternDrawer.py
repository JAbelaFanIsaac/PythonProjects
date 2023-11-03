import turtle
import random
turtle.speed(0)
arrayPattern = []

class pattern():
    def __init__(self, angle: int, times: int):
        self.__angle = angle # Integer
        self.__times = times # Integer

    def angler(self):
        message = int(self.__angle)
        return message

    def timing(self):
        message = int(self.__times)
        return message

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  # setting window dimensions
        turtle.bgcolor('black')
        for x in range(int(self.__times)):
            turtle.pencolor(colors[x % 6])
            turtle.width(x /100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
        turtle.done()

"""
mypattern = pattern(120, 100)  # Demo pattern
mypattern.draw_pattern()
"""
def Constructor():
    try:
        with open("patterns.txt") as file:
            for i in range(5):
                ang = file.readline().strip()
                tim = file.readline().strip()
                arrayPattern.append(pattern(ang, tim))
    except:
        print("Aint working")

Constructor()
j = random.randint(0,4)
first_angle = arrayPattern[j].angler()
first_time = arrayPattern[j].timing()
pattern_drawing = pattern(first_angle, first_time)
pattern_drawing.draw_pattern()
