import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
star = turtle.Turtle()
star.speed(0)
star.width(2)

# Set up colors
hue = 0
num_colors = 36

for i in range(180):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    star.color(color)
    star.forward(100)
    star.right(144)
    hue += 1/num_colors

# Hide turtle
star.hideturtle()

# Keep window open
turtle.done()