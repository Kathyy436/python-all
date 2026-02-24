import random
from colorama import Fore, Back, Style

"""
What do we need?

We need the wooden disks (30)
An array with different amounts of points (1, 2, 3, 4)
The box 8x4
Floor = 0
Port1 = 1
Port2 = 2
Port3 = 3
Port 4 = 4


Box =    [0,0,0,0],
         [1,2,3,4],
         [0,0,0,0],
    	 [0,0,0,0],
	     [0,0,0,0],
    	 [0,0,0,0]






	[


3 = strong
2 = medium
1 = weak

Accept column number
Accept strength (3-1)
Calculate sloth with maths
Reprint game board
Single player game
For loop
"""
def printBoard(box):
    print("------------------")
    for row in range(14):
        for col in range(4):
            if(box[row][col]=="D"):
                print(Fore.LIGHTCYAN_EX, box[row][col], end = " ")
            else:
                print(Fore.BLACK, box[row][col], end = " ")                  #Making the game board appear as an actual board
        print()
    print("------------------")
#end of function


disks = 30

box =[[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [1,2,3,4],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]
]                                   #The game board

strengths = [1,2,3]       #How strong you want to trow the disk

strenght = 0

tCount = 0


printBoard(box)

while(tCount< disks):      #as long as there are discs left...
    #Now, while disks are trown we have to ask
    print("Welcome to Sjoelen a board game that goes from bottom to top")
    print("Once the D(Disk) goes past the numbers 1,2,3 and 4 you get points based on the row number.")
    print("If the row I give you is 5, you will not see points (Because row 5 is the wall)! :P ")
    print("Have Fun!","Made by Kathy & Cloe")
    print()
    print("Do you want to trow?yes or no")
    answ = input()
    while answ.lower() not in ["yes", "no"]:
        print("Only input yes or no")
        answ = input()

    if answ.lower() == "no":
        print("That's fine, goodbye!")
        break
    else:
        print("Choose the strength you want to trow the disk with, 1 = weak, 2 = medium strength and 3 = strong:")
        strength = int(input())
                                                #choose one of the 4 columns randomly.

    printBoard(box) #each time i need to see status of grid, i call this function.
    col= random.randint(0,3)
    row = -1
    print(row, col)


    while strength<1 or strength>3:
            print("Error! 1-3 only")
            strength = int(input())              #We have to make sure they only enter 1-3input("Press to see the board...")
    if strength == 1:
        row = random.randint(9,13)#The disks have to glide further with a different amount of power.#
    elif strength ==2:
        row = random.randint(5,9)
    elif strength ==3:
        row = random.randint(0,5)
                                                #choose one of the 4 columns randomly.
    print(f"you chose {strength} and my row for you is {row}")
    input()

  # row = base_row
    if box[row][col] == 0 and row != 5:                          #I have to
        box[row][col] = "D"
    input("Press to see board...")
    printBoard(box)

    points = 0
    for r in range(5):
        for c in range(4):                       #first i had 4
            if box[r][c] == "D":
              points = points + (c+1) #First i had c+1
    print("You have", points, "points!! Good job!! :)")
    print(" ")


