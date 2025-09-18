import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Turtle Project - Shapes")

# Create turtle object
artist = turtle.Turtle()
artist.pensize(3)
artist.speed(2)

# Draw a square
artist.color("green")
for _ in range(4):
    artist.forward(100)
    artist.right(90)

# Move turtle to new position
artist.penup()
artist.goto(150, 0)
artist.pendown()

# Draw a circle
artist.color("red")
artist.circle(50)

# Hide turtle after drawing
artist.hideturtle()

# Keep window open until clicked
screen.exitonclick()