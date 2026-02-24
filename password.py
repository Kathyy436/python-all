#Kathy Meijer
#03/09/25
#Someone try's to crack your password

password = "WaterBottle"  #This is the password.
tries = 0               #Here is the number of tries that are already tried
max_tries = 3           #This is the amount of times I am allowed to guess my password.

while tries < max_tries:        #Here I say that as long as tries is less than the max amount of tries to use on a password, the operation under this will be performed
    attempt = input("Enter password:")  #Here is me asking the user to fill in their pw, with input
    if attempt == password:             # Here I say that if the input is correct, so the user has the right password, if that happens, the following operation will be followed.
        print("Acces granted!")           #You guessed right.
        break      #I told the loop to stop
    else:                       #if the if is wrong, do this
        print("Incorrect password, try again")
        tries += 1

if tries ==max_tries:                      #if there are as much tries as the max tries (3), it doesnt work anyore.
    print("Too many times tried, the software is now blocked.")




