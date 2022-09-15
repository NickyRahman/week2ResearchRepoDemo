import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn . bgcolor('black')
color = ['red', 'yellow', 'blue', 'green', 'pink']
t. speed(0)
for i in range(300):
    t.pencolor(color[i%5])
    t.circle(100)
    t.forward(i)
    t.left(160)
turtle.done()
