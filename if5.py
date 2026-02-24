"""
TASK 1
Write a Python program that does the following:
- Asks person's name and year of birth.
- If the person is less than 18, the message is "Sorry - X - you are not yet eligible to vote. You still have Y years left to vote."
- If the person is 18 or above the message should say "X, you are eligible to vote! You have been for Y years."
- Print a suitable error message if the age is less than 0 or over 100.
- Use meaningful variable names and user friendly messages.

TASK 2
Write a Python program that does the following:
- Asks a person's name
- Asks a person's weight (in KG) and height (in M)
- It then calculates the person's Body Mass Index (BMI) with the formula --> weight / (height * height)
- If BMI value is less than 18.5, print the message "X, you are underweight"
- If BMI value is between 18.5 and 24.9, print the message "X, you have normal weight."
- If BMI value is between 25 and 29.9, print the message "X, you are overweight."
- If BMI value is above 29.9, print the message "X, you are obese".
- Print a suitable error message if weight or height are less than 1.
- Use meaningful variable names and user friendly messages.
"""

#Kathy Meijer
#08/11/25
#Both tasks

name = input("Hey, what is your name?")       #Here I use input as an
yob = int(input("Hi", name, "what year were you born?"))

while yob>2025 and yob<1900:
    print("Error, you made a mistake, please re-enter")
    yob= int(input())
if yob < 2007 and yob>=2025:
    print("Sorry", name, "You are not eligible to vote. You still have", yob-2007, "years left to vote")
elif yob >= 2007 and yob<1900:
    print( name, "You are eligible to vote! You have been for", yob-2007, "years ")


