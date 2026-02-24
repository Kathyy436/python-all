

#Kathy Meijer
#26/08/25

print("What is your name?") #Asking a persons name
name = input()
print ("Hello", name)

print("What is your YOB?")

YOB = int(input("Enter YOB please (1900-2025)"))

age = 2025-YOB

if(age>=125):
    print("Sorry, that age does not exist")
if(age<=-1):
    print("Sorry, that age does not exist")

if(age>=18 and age<125):
    print(name, "You are eligeble to vote! You have been eligeble to vote for", age - 18, "years!")

if(age<=18 and age>=-1):
    print("Sorry", name, "You are not eligeble to vote, you still have", 18-age, "years left to vote")
