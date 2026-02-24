#kathy meijer
#18/11/25
#Selling lemonade


"""
(b) Write a program that performs the following operations:
(i) Asks the user to enter a flavor number (0-2).
(ii) Asks the user to enter how many cups of this flavor were sold.
(iii) Looks up the price for this flavor from the Prices list.
(iv) Calculates the total by multiplying cups with price for each cup.
(v) Loops steps (i) to (iv) until the user enters a -1 for flavor number.
(vi) Outside the loop it should print total money made along with individual
sales for each lemonade type with name (£).
(vii) No invalid flavor value (<-1 or >2) should be allowed and re-entered.

"""

#3 flavours:Strawbery, mint, watermelon
#3 prices:0.50, 1.00, 1.50

flavours = ["strawberry", "mint", "Watermelon"] #String type
cost = [0.50, 1.00, 1.50]    #float
sales = [0,0,0] #integer

#I need to setup the data


while True:
    fNo = int(input("Enter a flavour number (0-2)"))    # Here I ask what flavour is asked
    if(fNo==-1):
        break
    while(fNo<0 or fNo>2):
        fNo = int(input("Out of range, enter number (0-2)"))
    cups = int(input("How many cups of this flavour were sold?"))   # How many cups
    while(cups<0):
        cups = int(input("You can't have less cups, the minimum is 0. Re-enter."))
    prOfFlav = cost[fNo]

    sales[fNo]= sales[fNo] + (cups*prOfFlav)




print(sales)
print(f"You made £{sum(sales)}")





















