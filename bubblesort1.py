#21/10/25
arrays= [12, 34, 56, 23, 84, 11, 93]
size = len(arrays)
pass_=0



#make an outer loop to go through entire array
for i in range(0, size):
    # make an inner loop that goes from 0 until len-i
    for j in range(0, size-i-1):
        if(arrays[j]>arrays[j+1]):
            #swap these values
            arrays[j], arrays[j+1] = arrays[j+1], arrays[j]
        #the remaining arrays
    pass_=pass_+1
    print("After pass", pass_)
    print(arrays)
#outside the loops print the arrays
print(arrays)


for i in range(0, size):
    for j in range(0, size-i-1):
        if(arrays[j]>arrays[j+1]):
            arrays[j], arrays[j+1]=arrays[j+1], arrays[j]
        print(arrays)
print(arrays)


for i in range(0, size):
    for j in range(0, size-i-1):
        if(arrays[j]>arrays[j+1]):
            arrays[j], arrays[j+1] = arrays[j+1], arrays[j]
        print(arrays)
print(arrays)


for i in range(0, size0:
    for j in range(0, size-i-1):
        if(arrays











