#Kathy Meijer
#08/10/25
#Making a dish with a budget of 10 pounds

dish = input("Hello dear, what dish will you be making?")

items = []
quantities = []
costs = []

item=""
qty=0
cost=0

while(item!="done"):    #this is to take all items into 3 lists
    item = input("Enter item name:")
    if item == "done":
        break
    items.append(item)

    qty = int(input("Enter your quantity:"))
    while qty <=0:          #this is for
        qty = float(input("Enter your quantity:"))
    if qty == "done":
        break
    quantities.append(qty)


    cost = float(input("Enter the cost:"))
    while cost <=0:
       cost = float(input("Enter the cost:"))
    if cost == "done":
        break
    costs.append(cost)


print(items)
print(quantities)
print(costs)


input()


from prettytable import PrettyTable
table = PrettyTable()

table.field_names=["Items", "quantity", "cost"]
for index in range(len(items)):
    table.add_row([items[index], quantities[index], costs[index]])

print(table)

total = sum(costs)  #adds up all the values from the costs[ ] array/list
if total>10:
    difference = total-10
    print("Your total cost is", total, ", that is", difference, "more than your budget. You should watch out!")
if total==10:
    print("Perfect, exactly your budget!")
if total<10:
    difference = 10 - total
    print("Your total cost is", total, ", that is", difference,"less than your budget. Great job!")
print(total)


















