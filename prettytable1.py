#Kathy Meijer
#07/10/25

pets= ["Dogs", "Cats", "Birds", "Guinea pigs", "Hamsters"]              #list for animals
diet=["Carnivore", "Carnivore", "Seeds", "Herbivore", "Herbivore"]            #list for diets

print(pets)                          #prints the exact list
print(" ")

print(*pets)                   #prints all the words in between high commas
print(" ")

print(*pets, sep = ",")               #prints all the words in between high commas with commas
print(" ")

[print(i) for i in pets]                #prints all the words in a list
print(" ")

from prettytable import PrettyTable      #Adding a table to put our list in
table = PrettyTable()                  #variable name for prettytable

table.field_names=["house pets"]              #This will be the name on top of our table
for pet in pets:
    table.add_row([pet])                   #here we will add the list names pets in the table

print(table)
print(" ")


from prettytable import PrettyTable
table = PrettyTable()

table.field_names=["House pets", "Diet"]          #i made two lists, one for animals and one for diets
for index in range(len(pets)):                          #This is the code I used for adding in the pets
    table.add_row([pets[index], diet[index]])              #And here I am able to add both the tables to eachother


print(table)


