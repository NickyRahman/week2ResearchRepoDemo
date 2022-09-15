import turtle
tu = turtle.Turtle()         # we have now created an object for this turtle labeled as tu
tu.screen.bgcolor('black')   # we have chnaged the screen background color to black
tu.pensize(2)                # this is the pensize or line thickenss of the drawing
tu.color('green')            # this is the initial color of the turtle or the line being being drawn

#now when we start the drawing program, the turtle will be looking towards the right direction

tu.left(90)                  # now we turn the turtle arrow to face upward by making it turn left 90 degrees
tu.backward(100)             # now we move the turtle down 100 pixels. This will allow us to see the whole tree 'grow'
tu.speed(200)                # this is the speed of the drawing
tu.shape('turtle')           # we have changed the shape of the turtle arrow to an actual turtle

# we will use recursion function to draw the tree
def tree(i):
    if i<10:
        return               #this is the base condition to stop recursion so it does not keep drawing infinitely
    else:
        tu.forward(i)        # this will allow the turtle to draw the tree in forward direction
        tu.color('green')     # this will draw circular green flowers at the end of each branch/stem
        tu.circle(2)
        tu.color('brown')    # after drawing the green flower, we want the color to change to brown for the branches
 # Now we want to draw the tree growing in the left direction       
        tu.left(30)          # It will move left and draw the flower, and continue to move left and draw flower again till value of i is less than 10          
        tree(3*i/4)          # e.g value of i is 100 therefore 3*100/4 = 75; now value of i is 75 therefore 3*75/4 = 56.25; now value of i is 56.25 therefore 3*56.25/4... 
        tu.right(60)         # once the left side is done, the turtle will back back using the backward() command, and then it will go in the right direction
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)
tree(100)
turtle.done()

