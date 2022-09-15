#draw spiral patterns

import turtle

#set the environment
turtle.Screen().clear()
turtle.bgcolor ('black') #change window background to black
turtle.speed(0)
turtle.color ('red')
turtle.pensize(2)

#function to draw spiral patterns per input parameters
def Spiral(length, angle, step, min_length):    #parameters based on the presented algorithm above
    while(length > min_length):                 #loop through until the predefine minimum length
        turtle.forward(length)                       #draw side(s) of the pattern
        turtle.left(angle)                           #turn left an amount of 'angle'
        length = length - step                  #then, reduce the lenght and get a new lenght in each time

#call to test the function above with necessary parameters
Spiral(length = 250, angle = 89, step = 1, min_length = 32)



#create another spiral in blue at a new coordinate
turtle.penup()           #lift the pen up - don't create a line
turtle.pendown()         #bring the pen down to start drawing again
turtle.speed(0)
turtle.pensize(2)
turtle.goto(0,-250)      #move the turtle to new coordinate


#function to draw spiral patterns per input parameters
colors = ['purple', 'red', 'orange', 'blue', 'green', 'magenta', 'cyan']
    turtle.color(colors[length %7])         #use changes of lenght as an index of the color
       



