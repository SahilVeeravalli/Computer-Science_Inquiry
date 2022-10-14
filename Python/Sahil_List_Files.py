import random
from graphics import *
from random import randrange
def main():
    print("Please choose one of the following: \n 1. Find vowels in a sentence \n 2. Reverse a sentence \n 3. Create a list with random numbers \n 4. Draw Quiz scores \n 5. Write to a file \n 6. Quit the program") 
    choice = input("Which would you like to do: ")

    if choice == "1":
      findVowels()
    elif choice == "2":
      reverse()
    elif choice == "3":
      randomList()
    elif choice == "4":
      graph()
    elif choice == "5":
      writeToFile()
    elif choice == "6":
      quit()

      
def findVowels():
    sent = input("Please Enter Your Own Sentence: ")
    vowels = 0
  
    for i in sent:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
            or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
  
    print("Total Number of Vowels in this Sentence = ", vowels)

def reverse():
    s=input("Please Enter a sentence: ") # initial string
    stringlength=len(s) # calculate length of the list
    slicedString=s[stringlength::-1] # slicing 
    print (slicedString) # print the reversed string
    
def randomList():
    a = []
    print("Here is your random list: \n")
    for x in range(100):
        nums = random.randint(1,100)
        b = print(nums, end=" ")
        a.append(nums)
    print(a)
    print("This is the sum of the numbers: ", sum(a))
    print("This is the average: ", sum(a)/100)



    
def rand_color():
    return(color_rgb(randrange(256), randrange(256), randrange(256)))
def graph():
    win = GraphWin("window", 500, 500)
    line1 = Line(Point(50,50),Point(50,500))
    line1.setWidth(3)
    line1.draw(win)

    line2 = Line(Point(0,450),Point(500,450))
    line2.setWidth(3)
    line2.draw(win)
    x = 10
    x1 = 60
    for i in range (5):
        num = eval(input("Enter a number between 1 and 100 --> "))
        h = 4*num
        y = 450-h
        x = x + 80
        x1 = x1 + 80
        y1 = 450
        rect = Rectangle(Point(x,y),Point(x1,y1))
        rect.setFill(rand_color())
        rect.draw(win)
        text = Text(Point(x+25,y+20),num)
        text.setSize(10)
        text.setTextColor("red")
        text.draw(win)

def writeToFile():
    summary_list = ["Lists are very fun", "This text is generated","From a list","A list is changeable","It contains Items"]
    textfile = open("summary.txt", "w")
    for element in summary_list:
        textfile.write(element + "\n")
    textfile.close()

main()
while True:
    main()
    if input("Do you want to play again? (y/n): ") == "y":
        main()

