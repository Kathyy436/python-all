array = [89, 12, 14, 73, -5, 23, 45 ,67, 39]
size = len(array)
pass_=0
#make an outer loop to go trough outer loop
for i in range(0, size):
    #make an inner loop that goes from 0-len-i
    swapped=False
    for j in range(0, size-i-1):
        if(array[j]> array[j+1]):
            #swap these values
            array[j], array[j+1] = array[j+1], array[j]
            swapped=True  #set to true if swap happens
            #the remaining arrays
    pass_=pass_+1
    if(swapped==False):   #if inner loop came out with no swaps
        break
    print("After Pass", pass_)
    print(array)
print(array)


