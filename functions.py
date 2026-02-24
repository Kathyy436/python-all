#kathy meijer
#17/02/26
#practicing with functions


# I want to print a line of stars at different times in your program:
#*********************************************
#Best method:



def starLine():
    print("*********************************************")

starLine()
print("Hiii")
starLine()

print()

def smilyLine():
    print(":):):):):):):):):):):):):):):):):):):)")
def smilyLiny():
    print("(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:")

smilyLine()
print("How are you...")
smilyLiny()

print()
#Now i want to choose different symbols every time
def anyLine(c):                                #The c stand for the character I want to show
    for i in range(40):                         #How often I want the symbol to show (now fourty times)
        print(c, end = " ")                          #I am printing the symbol and ending it with a space every time, so they are not stuck to eachother now.
    print()

anyLine(":)")                         #Here is where I print which character, in the spacebars after the def function
print("HI")
anyLine("(:")

print()

#What if I want different lengths for both sides?

def anyLine(c, l):                                          #The c is the symbol for the character, the length is how often i want to make the carachter show.
    for i in range(l):                            #Now i don't have a set length, so I tell them I can choose the lenght
        print(c, end = " ")
    print()

anyLine(":)", 20)                             #The number is how often i want to print the character
print("HI")
anyLine("(:", 40)

"""

name = input()

def greeting(name):
    print("Hello", name, "!")

greeting(name)

time = int(input())


def greetTime(name, time):
    if time <= 8 or time >= 12:
        print("Good morning", name, "!")
    elif time <= 13 or time >= 16:
        print("Good afternoon", name, "!")
    elif time <= 17 or time >= 22:
        print("Good evening", name, "!")

"""

def printWord(c, l):
    for i in range(l):
        print(c, end = " ")
    print()

printWord("Hello", 15)
print("")
printWord("ISA", 200)

#I want the computer to give me the list of times table i ask it

def generateTable(num, times):
    for i in range(1, times + 1):
        print(num, "x", i, "=", num * times)
    print()

generateTable(10, 5)

#I am making a program which makes first puts last name and then the last name
def formatName(first, last):
    print(last+ ", "+ first)

formatName("Jennifer", "de Abreu")


#I want to write a program which accepts two numbers and a symbol, and the computer will answer.

n1 = int(input())
n2 = int(input())
sym = input()

def calculate(n1, n2, sym):
    if(sym == "+"):
        print(n1+n2)
    elif(sym == "-"):
        print(n1-n2)
    elif(sym == "x"):
        print(n1 * n2)
    elif(sym == "%"):
        print(n1 % n2)
    else:
        print(n1 / n2)

calculate(n1, n2, sym)

pound = int(input())

def poundDollar(pound):
    print(pound * 1.36 )
    print()

poundDollar(pound)














