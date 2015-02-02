import random
import turtle

finished = []

def draw_leaves():
    for turtle in finished:
        for i in range(20):
            turtle.begin_fill()
            rand = random.randint(-16, 16)
            turtle.color((16 + rand, 128 + rand, 16 + rand))
            turtle.circle(random.randint(4, 8), steps=5)
            turtle.left(36)
            turtle.penup()
            turtle.forward(random.randint(8, 20))
            turtle.pendown()
            turtle.end_fill()

def draw_branch(turtle, level=12):
    if level > 0:
        turtle.pensize(level)
        clone = turtle.clone()

        turtle.left(random.randint(1, 20))
        turtle.forward(random.randint(2, 8) * level)
        draw_branch(turtle, level-random.randint(1,3))

        clone.right(random.randint(1, 20))
        clone.forward(random.randint(2, 8) * level)
        draw_branch(clone, level-random.randint(1,3))
    else:
        turtle.pensize(1)
        finished.append(turtle)

def draw():
    turtle.setup(800, 600)
    turtle.colormode(255)
    turtle.bgcolor("white")
    turtle.pensize(13)
    turtle.color("brown")
    turtle.speed(1000)
    turtle.hideturtle()

    turtle.penup()
    turtle.right(90)
    turtle.forward(300)

    turtle.pendown()
    turtle.right(180)
    turtle.forward(250)
    draw_branch(turtle)
    draw_leaves()


draw()
