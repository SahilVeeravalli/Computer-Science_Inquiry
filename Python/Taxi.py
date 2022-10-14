from graphics import *#import the graphics library
from random import randrange #import random number generator
import time #import a time module
import math

def rand_color():
    return(color_rgb(randrange(256), randrange(256), randrange(256)))
def main():
    win = GraphWin("Taxi",500,500)
    win.setBackground('White') #This is the top of the snowman
##    p = win.getMouse() #Click inside the 
##    x = p.getX()
##    y = p.getY()
    p = win.getMouse() #Using corners to draw the rectangle
    q = win.getMouse()
    px = p.getX()
    py = p.getY()
    qx = q.getX()
    qy = q.getY()
    corner1 = p
    frame = Rectangle(p,q)
    frame.draw(win)
    frame.setFill("Yellow")

    baselen = (qx-px)  
    baseheight = (py-qy)
    wcoord1 = 0.25*baselen  #Using multiplication to get the coords of the wheels in relation to the base of the rectangle
    wrad = 0.1*baselen

    wcoord2 = 0.75*baselen
    wheel1 = Circle(Point(wcoord1+px,qy), wrad)
    wheel1.setFill("black")
    wheel1.draw(win)

    wheel2 = Circle(Point(wcoord2+px,qy), wrad)
    wheel2.setFill("black")
    wheel2.draw(win)

    z = win.getMouse() #Rectangle for the top frame
    zx = z.getX()
    zy = z.getY()
    frame2 = Rectangle(Point(px+0.25*baselen,zy), Point(px+.75*baselen, py))
    frame2.setFill("Yellow")
    frame2.draw(win)

    roofheight = (zy-py)
    frame2len = (zx-px)
    frame2len1 = (zx-px)

    w1coord1 = 0.28*baselen
    w2coord2 = 0.53*baselen

    w3coord1 = 0.5*baselen

    u = win.getMouse() #Places windowns next to each otehr
    ux = u.getX()
    uy = u.getY()
    gx = zy-py
    window1 = Rectangle(Point(w1coord1+zx,zy+.25*frame2len), Point(w1coord1+px,py-.25*frame2len))
    window1.setFill("Blue")
    window1.draw(win)


    f = win.getMouse()
    fx = f.getX()
    fy = f.getY()
    gx = zy-py
    window2 = Rectangle(Point(w2coord2+zx,zy+.25*frame2len), Point(w2coord2+px,py-.25*frame2len))
    window2.setFill("Blue")
    window2.draw(win)

    text = Text(Point(px+0.5*baselen,qy+baseheight*0.5), "TAXI") #Places text during the last click
    text.setSize(20)
    text.setTextColor("red")
    text.draw(win)
    
    win.getMouse()
    win.close()

main()

