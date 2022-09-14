import turtle
from random import randint

window = turtle.Screen() #open a new window
turtle.bgcolor("black") #change the background colour of the screen
turtle.color("yellow") #choose a colour for the star
turtle.speed(0) #how quickly the staris drawn

#the code to draw a single star
def draw_star():
    turns = 5
    turtle.begin_fill()
    while turns > 0:
        turtle.forward(25)
        turtle.left(145)
        turns = turns - 1
    turtle.end_fill()

#the code to draw 50 stas
num_stars = 0
while num_stars < 50:
    x = randint(-300, 300) #choose a random x-coordinate
    y = randint(-300, 300) #choose a random y-coordinate
    draw_star() #call up the draw_star function from above
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    num_stars = num_stars + 1

window.exitonclick() #close the window when clicked
