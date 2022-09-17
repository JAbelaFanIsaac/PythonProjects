import turtle
turtle.speed(0)
size = 6                  # size of the smallest square

def draw_multicolour_square(sz):
    """Make turtle t draw a multi-colour square of sz."""
    for i in ['red','blue','purple','green']:
        turtle.color(i)
        turtle.forward(sz)
        turtle.left(90)

for i in range(1000):
    draw_multicolour_square(size)
    size = size + 1          # increase the size for next time
    turtle.forward(5)        # move turtle along a little
    turtle.right(17)          # and turn a little
