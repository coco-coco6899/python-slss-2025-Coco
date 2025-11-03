# Python Turtle Artist
# Coco Woo
# Oct 28, 2025

import turtle

# Set up the environment
wn = turtle.Screen()
wn.bgcolor("lightblue")

rachel = turtle.Turtle()
rachel.turtlesize(3)

# create a dictionary of BUILDINGS colours
BUILDING_COLOURS = {
    "Tall": "#33658A",
    "Short": "#DFBE99",
    "thin": "#80B192",
    "thick": "#33658A",
}

rachel.speed(5)
rachel.width(3)

rachel.penup()
rachel.right(90)
rachel.forward(400)
rachel.right(90)
rachel.forward(800)
rachel.right(180)

rachel.pendown()
rachel.fillcolor("black")  # fill in the road
rachel.begin_fill()
rachel.forward(1500)
rachel.right(90)
rachel.forward(300)
rachel.right(90)
rachel.forward(1500)
rachel.right(90)
rachel.forward(300)
rachel.end_fill()

rachel.penup()
rachel.right(90)

rachel.forward(500)
rachel.right(90)

rachel.forward(80)

rachel.pendown()
rachel.fillcolor("white")
rachel.begin_fill()
rachel.right(90)
rachel.forward(200)
rachel.right(90)
rachel.forward(20)
rachel.right(90)
rachel.forward(200)
rachel.right(90)
rachel.forward(20)
rachel.end_fill()

rachel.penup()
rachel.left(90)
rachel.forward(400)

rachel.pendown()
rachel.fillcolor("white")
rachel.begin_fill()
rachel.left(90)
rachel.forward(20)
rachel.left(90)
rachel.forward(200)
rachel.left(90)
rachel.forward(20)
rachel.right(90)
rachel.forward(200)
rachel.end_fill()

rachel.penup()
rachel.right(180)
rachel.forward(650)

rachel.pendown()
rachel.fillcolor("white")
rachel.begin_fill()
rachel.left(90)
rachel.forward(20)
rachel.right(90)
rachel.forward(200)
rachel.right(90)
rachel.forward(20)
rachel.left(90)
rachel.forward(200)
rachel.end_fill()

rachel.penup()
rachel.right(180)
rachel.forward(500)
rachel.right(90)
rachel.forward(80)
rachel.right(90)
rachel.forward(400)
rachel.left(90)

rachel.pendown()
rachel.fillcolor("#7C7C7C")
rachel.begin_fill()
rachel.forward(100)
rachel.left(90)
rachel.forward(1500)
rachel.left(90)
rachel.forward(100)
rachel.left(90)
rachel.forward(1500)
rachel.end_fill()

rachel.penup()
rachel.left(90)
rachel.forward(300)
rachel.left(90)


def draw_a_thin_building(width: int, height: int, color: str):
    rachel.color(color)
    rachel.begin_fill()
    for _ in range(2):
        rachel.forward(width)
        rachel.left(90)
        rachel.forward(height)
        rachel.left(90)
    rachel.end_fill()


draw_a_thin_building(75, 225, "#9BA7C0")

rachel.penup()
rachel.goto(0, 0)
rachel.goto(200, -320)
rachel.left(180)

draw_a_thin_building(75, 225, "#9BA7C0")

rachel.penup()
rachel.goto(-100, -370)
rachel.right(360)


def draw_a_long_building(width: int, height: int, color: str):
    rachel.color(color)
    rachel.begin_fill()
    for _ in range(2):
        rachel.forward(width)
        rachel.left(90)
        rachel.forward(height)
        rachel.left(90)
    rachel.end_fill()


draw_a_long_building(100, 500, "#33658A")

rachel.penup()
rachel.goto(-350, -350)
rachel.right(270)


def draw_a_thick_building(width: int, height: int, color: str):
    rachel.color(color)
    rachel.begin_fill()
    for _ in range(2):
        rachel.forward(width)
        rachel.left(90)
        rachel.forward(height)
        rachel.left(90)
    rachel.end_fill()


draw_a_thick_building(300, 700, "#2A2E45")

rachel.penup()
rachel.goto(270, -360)
rachel.right(90)

draw_a_thick_building(300, 700, "#2A2E45")

rachel.penup()
rachel.goto(500, -380)

draw_a_long_building(100, 500, "#33658A")


def draw_a_short_building(width: int, height: int, color: str):
    rachel.color(color)
    rachel.begin_fill()
    for _ in range(2):
        rachel.forward(width)
        rachel.left(90)
        rachel.forward(height)
        rachel.left(90)
    rachel.end_fill()


rachel.penup()
rachel.goto(-300, -350)
draw_a_short_building(200, 225, "#2A2E45")

rachel.penup()
rachel.goto(-360, -380)

draw_a_thin_building(75, 225, "#9BA7C0")

rachel.penup()
rachel.goto(-550, -370)

draw_a_long_building(200, 500, "#33658A")

rachel.penup()
rachel.goto(-10, -350)

draw_a_short_building(225, 300, "#7C9EB2")


wn.exitonclick()
