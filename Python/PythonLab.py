from graphics import *#import the graphics library
import random #import random number generator

def main():
    win = GraphWin("PyLab",500,500)
    win.setBackground('White')
    a = random.randint(0, 7)
    b = random.randint(0, 7)
    c = random.randint(0, 7)
    d = random.randint(0, 7)
    nums = [a, b, c, d]
    print (nums)

    p = win.getMouse()
    px = p.getX()
    py = p.getY()
    z = 0

    square1 = Rectangle
    
    outer = Rectangle(p, Point(px+100,py+100))
    outer.draw(win)
    outer.setFill("Yellow")

    for i in nums[a]:
        outer = Rectangle(p, Point(px+90,py+90))
        outer.draw(win)
        outer.setFill("Yellow")
    

main()

    
