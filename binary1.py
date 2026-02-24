#KathyMeijer
#12/11/25
#Working with a faster type of sort, binary sort


import random

"""
array = []                 #This is an empty list
for i in range(1000):            #With this code I want the computer to give me random numbers
    array.append(random.randint(1, 1000))
array.sort()

numberfind = 234           #This is the number I want the pc to find
lowest = 0
highest = len(array)                #Here i told the pc where the lowest and highest numbers are in the array
middle = (lowest+highest)//2       #Here i get the middle number, so that is where the computer can start

found = False

while(lowest<=highest):                           #while the lowest number is less or equal to the highest number,
    print("Checking the middle now!")
    if(array[middle]==numberfind):              #if the middle of the list is the number i want to find
        print("Found!")
        print("It was in position", middle)
        found = True
        break                              #and break the whole system
    if(array[middle]<numberfind):                #if the middle of the list is less than the number I want to find
        print("Oops! Turning right from", middle)       #Telling me what number they are at
        lowest = middle+1                       #The lowest number turns in to the middle number plus one
    if(array[middle]>numberfind):
        print("Turning left from", middle)
        highest = middle-1
    middle(lowest+highest)//2


if found==False:
    print("Not found")


#This was the code with numbers
"""



names = ["Chloe", "Deepan", "Eduardo", "Jonathan", "Kathy", "Lara Mae", "Nathan", "Nico",]

namefind = "Kathy"
lowest = 0
highest = len(names)
middle = (lowest+highest)//2

while(lowest<=highest):
    print(middle)
    if(names[middle]==namefind):
        print("Found!", namefind)
        break

    if(names[middle]<namefind):
        lowest = middle+1

    if(names[middle]>namefind):
        highest = middle-1

    middle= (lowest+highest)//2





