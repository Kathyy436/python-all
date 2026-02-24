#My name is Kathy Meijer
#20/08/25
#Calculator

#print("Enter first number please:") or num1 = input("Enter first number please")

num1 = input("Enter first number please") #This prints and
num2 = input("Enter second number please")

#Now we print the different calculations
print("Sum :", sum)
#now the calculaton whent wrong because they added the numbers to eachother instead of saying plus. For example, 12+13 becomes 1213 instead of 25.
#we want it to be 25, so how do we do that?
sum = int(num1) + int(num2)
#If we dont add int, it won't add up.
sum = int(num1)+int(num2)
print(num1," + ",num2, "=", sum)

sum = int(num1)-int(num2)
print(num1," - ",num2, "=", sum)

sum = int(num1)*int(num2)
print(num1," * ",num2, "=", sum)

sum = int(num1)/int(num2)
print(num1,"/",num2, "=", sum)

sum = int(num1)%int(num2)
print(num1,"%",num2, "=", sum)















