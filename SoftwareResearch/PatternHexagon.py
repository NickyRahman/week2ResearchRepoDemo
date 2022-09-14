import turtle
t = turtle.Turtle()

#change window background to black
turtle.bgcolor ('black')

#draw four circles and fill with colours
list1 = ['purple', 'red', 'orange', 'blue', 'green']
for i in range(200):
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
