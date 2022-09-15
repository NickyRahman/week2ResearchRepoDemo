#import library
from turtle import *

#select colors
colors = ['red', 'yellow', 'green', 'blue', 'purple', 'pink']

#starting loop
for i in range(126):
    bgcolor('black')
    pencolor(colors [i % 6])
    width(i / 5 + 1)
    forward(i)
    left(20)

    #set speed
    speed(10)

    #end the program
    done()
