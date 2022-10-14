from time import time, localtime, strftime
import datetime
def main():
        a = " 1. Compute price of an item\n"
        b = "2. Compute shadow of an object\n"
        c = "3. Print out greetings\n"
        d = "4. Compute salary of an employee\n"
        e = "5. Run all functions\n"
        print(a, b, c, d, e)
    
        choice = input('Please choose 1, 2, 3, 4, or 5: ')

        if choice == "1":
            computePrice(6, 5)
            
        elif choice == "2":
            shadowLength(2)
                                    
        elif choice == "3":
            greeting()
            
        elif choice == "4":
            salary(42)
            
        elif choice == "5":
            computePrice(6, 5)
            shadowLength(2)
            greeting()
            salary(42)
                   
    
def computePrice(item, price):
    item = int(item)
    price = float(price)
    print(item*price)

def shadowLength(height):
    height = float(height)
    t = time()
    elapsed = time() - t
    Time = strftime("%H", localtime(t))
    Time = float(Time)
    print(Time*height, "meters")

def greeting():
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greet = "Good morning"
    elif hour < 18:
        greet = "Good afternoon"
    else:
        greet = "Good night"    

    print(greet)
   

def salary(hours):
    hours = int(hours)  
    
    if hours <= 40:
        print("Your weekly salary is: ", hours*11.30, "Dollars")
    elif hours > 40:
        print("Your Weekly Salary is: ", (40*11.30)+(hours-40)*16.95, "Dollars")
main()
    