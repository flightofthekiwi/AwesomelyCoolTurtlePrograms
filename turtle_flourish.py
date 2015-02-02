import turtle
import random

def striangle(brad,depth,base,col):
brad.speed(1000000)
if col==0:
brad.color('red',(255,128,random.randint(0,255)))
else:
brad.color('blue',(random.randint(0,255),128,255))

brad.down()
if depth == 0:
brad.fill(1)
for i in 0,1:
brad.forward(base)
brad.left(20)
brad.forward(base)
brad.left(160)
brad.fill(0)
else:
for i in 0,1:
striangle(brad,depth-1,base,col)
brad.up()
brad.forward(base+depth+5)
brad.left(310)
brad.down()
return

def sstr(brad,depth,base):
brad.speed(1000000)
brad.color('green',(random.randint(0,255),255,128))
brad.down()
if depth == 0:
brad.fill(1)
for i in 0,1:
brad.forward(base)
brad.right(20)
brad.forward(base)
brad.right(160)
brad.fill(0)
else:
for i in 0,1:
sstr(brad,depth-1,base)
brad.up()
brad.forward(base+depth+5)
brad.right(310)
brad.down()
return

def run():
window = turtle.Screen()
window.colormode(255)
brad = turtle.Turtle()
brad.speed(1000000)
brad.pensize(1)
col = 255
striangle(brad,8,50,0)
sstr(brad,8,50)
striangle(brad,8,50,1)
window.exitonclick()

turtle.reset()
run()

