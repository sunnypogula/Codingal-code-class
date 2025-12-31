import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
heart = turtle.Turtle()
heart.speed(2)
heart.color("red")
heart.begin_fill()

# Draw the heart
heart.left(50)
heart.forward(100)
heart.circle(40, 180)
heart.left(260)
heart.circle(40, 180)
heart.forward(100)

# Fill the heart
heart.end_fill()

# Hide the turtle
heart.hideturtle()

# Keep the window open
turtle.done()