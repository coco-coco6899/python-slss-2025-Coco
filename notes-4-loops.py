# Coco Woo
# OCt 14


import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightyellow")

# TMNT - turtles
# create a turtle called Rachel
rachel = turtle.Turtle()
rachel.turtlesize(10)
# rachel.shape("turtle")
rachel.color("pink")

# move rachel around
# rachel.speed(1)
# rachel.width(3)
# rachel.penup()
# rachel.forward(200)
# ( rachel.right(45)
# rachel.forward(200)
# achel.right(45)
# rachel.forward(200)
# rachel.right(45)
# rachel.forward(350)
# rachel.right(90)
# rachel.forward(350)
# rachel.right(45)
# rachel.forward(200)
# rachel.right(45)
##rachel.forward(250) )

# for _ in range(5):
# rachel.forward(300)
# rachel.right(144)

# rachel.circle(100)
# rachel.penup()
# rachel.goto(125, 175)
# rachel.pendown()
# rachel.circle(100)
# rachel.penup()
# rachel.goto(100, 200)


## Turtle Methods


# rachel = turtle.Turtle()  # creates a turtle object

# # change attributes
# rachel.size()
# mikey.color()
# mikey.width()
# mikey.penup()    # mikey.pu()
# mikey.pendown()  # mikey.pd()
# mikey.shape()

# # actions
# mikey.forward()  # mikey.backward()
# mikey.left()     # mikey.right()
# mikey.circle()
# mikey.goto()


# Cookie making
# Set the colour of our choco chip cookie
# create a function to make cookie
def make_cookies(x: int, y: int):
    # for counter in range(100):
    # counter = counter * 50
    rachel.color("brown")
    rachel.speed(1)

    rachel.shapesize(1)
    rachel.pu()
    rachel.setheading(0)  # make sure Rachel point east
    rachel.penup()
    rachel.goto(-5 + x, -30 + y)
    rachel.pd()
    rachel.circle(30)
    # Draw a circle to represent our cookie
    rachel.pu()
    rachel.goto(10 + x, 10 + y)
    rachel.pd()
    rachel.stamp()

    rachel.pu()
    rachel.goto(10 + x, -10 + y)
    rachel.pd()
    rachel.stamp()

    rachel.pu()
    rachel.goto(-10 + x, -10 + y)
    rachel.pd()
    rachel.stamp()

    rachel.pu()
    rachel.goto(-10 + x, 10 + y)
    rachel.pd()
    rachel.stamp()

    rachel.pu()
    rachel.goto(0 + x, 0 + y)
    rachel.pd()
    rachel.stamp()


for counter in range(50):
    counter = counter * 50
    make_cookies(0, 0)
    make_cookies(100, 100)
    make_cookies(-100, -100)
    make_cookies(-100, 100)
    make_cookies(100, -100)

# Put a choco chip at the top right
# also bottom right , bottom left and top left
window.exitonclick()
