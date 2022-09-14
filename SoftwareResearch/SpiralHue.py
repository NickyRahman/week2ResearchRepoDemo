from turtle import *
import colorsys
bgcolor('black')
speed(0)
pensize(1.5)

hue = 0.0

for i in range(300):
    color = colorsys.hsv_to_rgb(hue,1,1)
    pencolor(color)
    hue += 0.01
    right(i)
    circle(75,i)
    forward(i)
    left(91)

done()



