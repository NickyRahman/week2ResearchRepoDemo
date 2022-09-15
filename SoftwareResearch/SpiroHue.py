#import library
from turtle import *

#set color
colors = ['red', 'yellow', 'green', 'red', 'yellow', 'green']

#set background color
bgcolor('black')

#Starting loop
for x in range(360):
    pencolor(colors[x % 6])
    width(x//100 + 1)
    forward(x)
    left(59)
    speed(5000)
done()