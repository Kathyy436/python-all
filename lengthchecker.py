#Kathy Meijer
#24/02/26
#Using a function to receive information and to return
"""
#function the body with def
def countWordLen(wordArray):
    counter = 0           #Keeping track of how much words
    #I have to loop it from 0 until the array size I want
    for i in range(0, len(wordArray)):
        if(len(wordArray[i])>=10):
            counter = counter + 1

    return counter
#End of the function

print(countWordLen(["HI", "BYE", "TOMORROW", "TODAY", "yesterday", "week"]))
print(countWordLen(["Football", "Basketball", "Dance", "Tennis", "Badminton", "Rugby", "Gymnastics", "Hockey"]))


#I need to make a code that is able to receive all functions and only give back the letter i want

def displayContacts(contactList, letter):
    newList=[]
    #step 1: loopt through list
    #step 2: check each word and see if its first letter matches "letter"
    #step 3: keep an empty list and add it to that list (append)
    #step 4: return the new list
    for i in range(len(contactList)):            #step 1
        if(contactList[i][0].lower()==letter.lower()):          #step 2
            newList.append(contactList[i])           #step 3
    return newList   #step 4



print(displayContacts(["Aria Bennett", "Marcus Delgado", "Leila Hassan", "Ethan Caldwell", "Sofia Marin", "Julian Park", "Naomi Fischer", "Dominic Russo", "Chloe Whitaker", "Xavier Brooks"], "M"))  #function call
"""

"""
1. The "Nicknamer" 📛
Goal: Create a function that takes a first name and a last name and returns a "cool" combined nickname.
The Task: Write a function make_nickname(first, last).
The Logic:
Take the first 3 letters of the first name and the last 3 letters of the last name.
Combine them and return the answer.
Example: make_nickname("Taylor", "Swift") should return "Taysft".
"""
"""
print("first name")
first = input()
print("last name")
last = input()



#The body of the function
def makeNickname(first, last):
    ft = first[0:3]
    lt = last[0:3]
    return(ft+lt)

print(makeNickname(first, last))

ans = makeNickname(first,last)  #call the function
print(ans)

"""
"""
2. The Movie Ticket Calculator 🍿
Goal: Practice using if/else inside a function with a return value.
The Task: Write a function get_ticket_price(age).
The Logic:
If age is under 12, return £8.
If age is 12 to 18, return £10.
If age is over 18, return £15.
Bonus: Add a second parameter is_wednesday (boolean). If it's True, subtract £2 from any price!
"""


def  getTicketPrice(age):
    if age <12:
        return("£8")
    elif age >= 12 and age <18:
        return("£10")
    else:
        return("£15")

print(getTicketPrice(18))































