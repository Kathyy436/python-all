#Kathy Meijer
#08/09/25
#Teaching Max the times table
'''
OPTION 1
Max is learning the times table. He can use a program that asks him for a number between 1 and 10 and then prints the times table for it.
Please write a program for the above requirement using a WHILE loop.

The program should validate the input Max provides so that any value < 1 or > 10 is rejected and re-accepted.

SAMPLE OUTPUT
Enter a number you want the times table for (1-10 only):  51
Error: 1-10 only please: 5

Enter a number you want the times table for (1-10 only):  5

5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
'''


print("Hey! What is your name?")
name = input()
print("Hey", name)

print("Enter a number you want for the time table (1-10)")  #Here I ask for the number, the first mistake I made was that I forgot to put int(input()). I did number = input()
number = int(input())



while number<1 or number>10:      # The loop, an error
    print("Error: 1-10 only please")
    number = int(input())

counter = 1

while counter<=100:
    product = counter * number
    print(number, "x", counter, " =", product)
    counter = counter + 1   #counter +=1















