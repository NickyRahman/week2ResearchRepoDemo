import turtle
import random
nicky = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

#set background colour
turtle.bgcolor('black')


#set colours for turtle
nicky.color('red', 'blue')

#set pen width
nicky.width(5)

#fill in shape with colour
nicky.begin_fill()
nicky.circle(50)
nicky.end_fill()

nicky.penup()
nicky.forward(150)
nicky.pendown()

nicky.color('yellow', 'green')

nicky.begin_fill()
for x in range(4):
    nicky.forward(100)
    nicky.right(90)
nicky.end_fill()

for x in range(10):
    randColor = random.randrange(0, len(colors))
    nicky.color(colors[randColor], colors[random.randrange(0, len(colors))])
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    nicky.penup()
    nicky.setpos((rand1, rand2))
    nicky.pendown()
    nicky.begin_fill()
    nicky.circle(random.randrange(0, 80))
    nicky.end_fill()
