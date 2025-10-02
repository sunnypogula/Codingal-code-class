import turtle

sc = turtle.Screen()
# creating canvas
sc.bgcolor("pink")

sc.setup(700, 700)

turtle.title("welcome to turtle window")

#turtle object creation
board = turtle.Turtle()
 
n  = 10
#creating a square
for i in range(0,n):
    board.forward(100)
    board.left(360/n)

turtle.done()