from graphics import *#import the graphics library
from random import randrange#import random number generator
def rand_color(): #Chooses Random Color
     return(color_rgb(randrange(256), randrange(256), randrange(256)))
def sampleloop(): #Loops through random numbers and adds it to the list
    f=[]
    for i in range(4):
        f.append(randrange(1,9)) #Chooses random numbers and adds them to a list
    return(f)

def main(): #Makes window 
    f=sampleloop()
    print(f)
    win = GraphWin("PyLab",500,500)
    win.setBackground('White')

    for m in range(len(f)): #amount of times to make square modules
        p=win.getMouse()
        x=p.getX()
        y=p.getY()
        k=0 #variable used to set the sizes of squares inside

        for i in range(f[m]): #Keeps making circles with pixel amount changes for squares inside the square modules
            square=Rectangle(Point((x+k), (y+k)), Point((x+125-k), (y+125-k)))
            square.setFill(rand_color())
            square.draw(win)
            k=k+8 #Offset for every square inside
    p2=win.getMouse()
    win.close() #Closes window
main()
        
    
