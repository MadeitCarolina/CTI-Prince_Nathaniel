import turtle

# Set up the turtle window
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()

# Draw the square
t.pensize(2)
t.color("blue")
for _ in range(4):
    t.forward(100)
    t.left(90)

# Move the turtle to a new position for the triangle
t.penup()
t.goto(150, 0)
t.pendown()

# Draw the triangle
t.color("red")
for _ in range(3):
    t.forward(100)
    t.left(120)

# Finish the drawing
t.hideturtle()
turtle.done()




