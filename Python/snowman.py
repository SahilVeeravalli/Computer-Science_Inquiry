from graphics import *#import the graphics library
import random #import random number generator
import time #import a time module

win = GraphWin("Snowman",500,500)

def main():
    win.setBackground('Blue') #This is the top of the snowman
    top = Circle(Point(250,120), 50)
    top.setFill("White")
    top.draw(win)
    
    middle = Circle(Point(250,240), 70) #This is the middle of the snowman 
    middle.setFill("White")
    middle.draw(win)
    
    bot = Circle(Point(250,400), 90) #This is the bottom
    bot.setFill("White")
    bot.draw(win)
    
    ground1 = Circle(Point(500,500), 120) #Part of the Ground
    ground1.setFill("White")
    ground1.setOutline("White");
    ground1.draw(win)
    
    ground2 = Circle(Point(0,500), 150)#Part of the Ground
    ground2.setFill("White")
    ground2.setOutline("White");
    ground2.draw(win)
    
    ground3 = Circle(Point(150,500), 90) #Part of the Ground
    ground3.setFill("White")
    ground3.setOutline("White");
    ground3.draw(win)
    
    ground4 = Circle(Point(350,500), 135) #Parth of the Ground
    ground4.setFill("White")
    ground4.setOutline("White");
    ground4.draw(win)
    
    but1 = Circle(Point(250,350), 10) #Button on snowman
    but1.setFill("Black")
    but1.setOutline("Black");
    but1.draw(win)

    but2 = Circle(Point(250,275), 10) #Button on Snowman
    but2.setFill("Black")
    but2.setOutline("Black");
    but2.draw(win)

    but3 = Circle(Point(250,240), 10) #Button on snowman
    but3.setFill("Black")
    but3.setOutline("Black");
    but3.draw(win)

    but4 = Circle(Point(250,205), 10) #Button on Snowman
    but4.setFill("Black")
    but4.setOutline("Black");
    but4.draw(win)

    but5 = Circle(Point(230,110), 10) #Button on Snowman
    but5.setFill("Black")
    but5.setOutline("Black");
    but5.draw(win)

    but6 = Circle(Point(270,110), 10) #Button on Snowman
    but6.setFill("Black")
    but6.setOutline("Black");
    but6.draw(win)

    
    nose = Polygon(Point(240, 140), Point(250, 120), Point(245, 145)) #Nose triangle
    nose.setFill('red')
    nose.setOutline('red')
    nose.setWidth(4)  # width of boundary line
    nose.draw(win)

    mouth = Oval(Point(240, 165), Point(260, 150)) # set corners of bounding box
    mouth.setFill('Red')
    mouth.setOutline("Black")
    mouth.draw(win)

    hat = Polygon(Point(225, 20), Point(215, 68), Point(280, 68)) #Hat on Snowman
    hat.setFill('red')
    hat.setOutline('black')
    hat.setWidth(4)  # width of boundary line
    hat.draw(win)

def makeSnow(): #This function makes the snow and generates them and puts them into a list
    listOfRect = [];
    for i in range (150):
        corner1 = random.randint(0, 500);
        corner2 = random.randint(0, 500);
        listOfRect.append(Rectangle(Point(corner2 + 10, corner1), Point((corner2 + 12), (corner1 + 30))))
        listOfRect[i].setFill('White');
        listOfRect[i].setOutline('White')
        listOfRect[i].draw(win)
    animateSnow(listOfRect)

def makeMoreSnow(listOfRect): #This function clears the list and generates new snow
        listOfRect.clear()
        for i in range (150):
            corner1 = random.randint(0, 500);
            corner2 = random.randint(0, 500);
            listOfRect.append(Rectangle(Point(corner2 + 10, corner1), Point((corner2 + 12), (corner1 + 30))))
            listOfRect[i].setFill('White');
            listOfRect[i].setOutline('White')
            listOfRect[i].draw(win)
            time.sleep(0.02);
        animateSnow(listOfRect)

            
def animateSnow(listOfRect): #Goes through the list and animates the snow
        for x in range (len(listOfRect)):
            listOfRect[x].move(0, 250);
            time.sleep(0.01)
        makeMoreSnow(listOfRect)

main()
makeSnow()
win.close()
