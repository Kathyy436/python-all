#Input --> integer for accept how many people are coming
#INPUT -->

people = int(input("How many people?"))
adults = int(input("Adults?"))
students = int(input("Students?"))
seniors = int(input("Seniors?"))


rating = input("Movie rating?")

TotalBill=0

if(Adults+children+seniors+student!=people):
    print("Wrong amount of people, please restart")
    else:
    if(rating =="18"):
        TotalBill = (Adults*10+children*3+seniors*8+students*5)
