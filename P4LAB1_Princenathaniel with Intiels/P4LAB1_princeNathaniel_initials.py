import turtle

# Set up the turtle window
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()

# Draw the first initial (N)
t.pensize(2)
t.color("blue")
t.penup()
t.goto(-200, 0)
t.pendown()
t.setheading(90)  # Face upward
t.forward(100)
t.right(135)
t.forward(140)
t.left(135)
t.forward(100)

# Move to a new position for the second initial (P)
t.penup()
t.goto(100, 0)
t.pendown()

# Draw the second initial (P)
t.setheading(90)  # Face upward again
t.forward(100)
t.right(90)
t.circle(-25, 180)

# Finish the drawing
t.hideturtle()
turtle.done()
