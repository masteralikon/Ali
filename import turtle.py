import turtle

t = turtle.Turtle()
t.begin_fill()
t.color("red")
t.left(45)
t.forward(100)
t.circle(50, 180)
t.right(90)
t.circle(50, 180)
t.forward(100)
t.end_fill()

turtle.done()