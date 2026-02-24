#enter temperature is inuput, it is a float
#OUTPUT is warmest/coldest at what time


#INPUTS
v1 = float(input("Enter temp for 12 PM"))
v2 = float(input("Enter temp for 1 PM"))
v3 = float(input("Enter temp for 2 PM"))
v4 = float(input("Enter temp for 3 PM"))
v5 = float(input("Enter temp for 4 PM"))
v6 = float(input("Enter temp for 5 PM"))
v7 = float(input("Enter temp for 6 PM"))

max = v1
if(v2>max):
    max=v2
if(v3>max):
    max=v3
if(v4>max):
    max=v4
if(v5>max):
    max=v5
if(v6>max):
    max=v6
if(v7>max):
    max=v7

min = v1
if(v2<min):
    min=v2
if(v3<min):
    min=v3
if(v4<min):
    min=v4
if(v5<min):
    min=v5
if(v6<min):
    min=v6
if(v7<min):
    min=v7


print("The highest temperature is", max, "the lowest temperature is", min, ".")