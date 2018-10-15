import turtle
import numpy as np
import colorsys
import multiprocessing
import time

POINTCOUNT = 500 #amount of points
RADIUS = 400 #pixels
MULT = 100 #multiplier

def circlePoints(n, r):
    # e^(2πi*k/n) where k € [0, n> gives the corners
    # of a perfect unit n-gon in the complex plane.
    return [r * np.e**( 2*np.pi * k * 1j /n ) for k in range(n)]

def main(POINTCOUNT, RADIUS, MULT, save=False, filename="terry.eps"):
    """draws a circle of radius [radius], and draws a mandelbrot-line-thing on a circle,
with [pointcount] points evenly spaced along the circle and [mult] as the multiplier
for the target endpoint for each line
returns the turtle, in case you want to do anything to it
Treat terry responsibly okay ಠ_ಠ"""
    # -p.real because angles start at (1,0) and we want to start at (-1,0) to  match the video
    # p.real is the x-coord and p.imag is the y-coord, in a complex plane.
    points = [(-p.real, p.imag) for p in circlePoints(POINTCOUNT, RADIUS)]
    points = list(points)

    #generate a color for each line, iterating over the hue with constant saturation and value
    colors = [colorsys.hsv_to_rgb(i/POINTCOUNT, 1.0, 0.6) for i in range(POINTCOUNT)]

    terry = turtle.Turtle()
    if POINTCOUNT > 40:
        terry.speed(0) #saves time
    else:
        terry.speed(POINTCOUNT//3)
    terry.pensize(1)
    if POINTCOUNT>200:
        turtle.tracer(False) #saves a LOT of time
        
    screen = terry.getscreen()
    canvas = screen.getcanvas()
    screen.screensize(2.2*RADIUS, 2.2*RADIUS)

    #DRAWING:
    terry.up()
    # turtle.circle starts at the bottom of the circle
    terry.goto(terry.xcor(), terry.ycor() - RADIUS) 
    terry.down()
    terry.circle(RADIUS)

    #draw each line
    for i in range(POINTCOUNT):
        x1,y1 = points[i]
        x2,y2 = points[i*MULT%POINTCOUNT]
        terry.up()
        terry.color(colors[i])
        terry.goto(x1,y1)
        terry.down()
        if POINTCOUNT < 100: terry.dot(6,"red")
        terry.goto(x2,y2)

    terry.up()
    terry.ht()
    return terry

    if save:
        canvas.postscript(file=filename, x=-RADIUS, y=-RADIUS, width=2*RADIUS, height=2*RADIUS, pagewidth=2*RADIUS, pageheight=2*RADIUS)
        
if __name__ == "__main__":
    for MULT in range(MULT):
        turtle.clearscreen()
        main(POINTCOUNT, RADIUS, MULT)
        
