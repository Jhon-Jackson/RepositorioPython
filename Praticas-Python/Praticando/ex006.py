import turtle, colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

h = 0
for i in range(360):
    t.pencolor(colorsys.hsv_to_rgb(h, 1, 1))
    t.circle(150)
    t.left(10)
    h = (h + 1/36) % 1

turtle.done()