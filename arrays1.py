#Kathy Meijer
#13/11/25
#Different methods

"""

OPTION 1
Jake collects stamps from different countries and wants a program that allows him to store information on them. Write a program that meets the following requirements.

- Has 4 arrays called --> Country, Value, Year Issued and Quality (1-3. 1 means poor condition and 3 means excellent condition)
- Allows Jake to enter data for each stamp into the array using a WHILE loop.
- Prints out all the information using a Pretty Table once the entries are done.
- Sorts the data by country name using a Bubble Sort and displays the sorted list.

"""

from prettytable import PrettyTable
table = PrettyTable()

countries = []
values = []
yeiss = []
qualities = []

country =""
value = 0
yeis = 0
quality = 0


while(country!="stop"):
    country = input("Enter country name, say stop if you have entered all of the countries:")
    if country == "stop":
        break
    countries.append(country)
    value = float(input("Enter value"))
    values.append(value)
    yeis= int(input("Enter year issued"))
    yeiss.append(yeis)
    quality = int(input("Enter the quality 1-3 (1 is very poor, 3 = excellent"))
    if(quality>3 or quality<1):
        print("You can only choose numbers 1-3")
        quality = int(input("Enter the quality 1-3"))
    qualities.append(quality)


for i in range(len(countries) - 1):
    for j in range(len(countries) - i - 1):
        if countries[j].lower() > countries[j + 1].lower():
            countries[j], countries[j + 1] = countries[j + 1], countries[j]
            values[j], values[j + 1] = values[j + 1], values[j]
            yeiss[j], yeiss[j + 1] = yeiss[j + 1], yeiss[j]
            qualities[j], qualities[j + 1] = qualities[j + 1], qualities[j]

table.field_names=["Countrys", "Values", "Year issued", "Quality"]
for index in range(len(countries)):
    table.add_row([countries[index], values[index], yeiss[index], qualities[index]])

print(table)
print("Sorted list by country name:")






