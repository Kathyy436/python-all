Large = 0
Small = 10000000000
for i in range( 100):
    Num = int(input())
    if Num > Large:
        Large = Num
    if Num < Small:
        Small = Num

print(Large, "is the largest")
print(Small, "is the smallest")