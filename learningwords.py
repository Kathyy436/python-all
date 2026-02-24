"""
Context: Bethany is learning her alphabet. She is working on the letter H. 

Challenge: Write a program that allows her to enter 10 words starting with H. The program stores all 10 words into a list. It then prints out the words sorted by ascending length of the word .

Example: “Harvest”, “Hello”

List should contain→ [“Hello”, “Harvest”]



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
"""
"""
print("Hello, your name please")
name = input()
print("Hi", name, ", you are going to practice the letter h. When you have typed as much words as you want that start with h, you type done and the words will be put into a list. Have fun!")

letterh = []

h = ""

for i in range(0,10):
    h = input("Enter word")
    while(h[0] not in ["h", "H"]):
        h = input("Wrong word. Please reinput")    
    
    letterh.append(h)

print(letterh)
size = len(letterh)

for i in range(0, size):
    # make an inner loop that goes from 0 until len-i
    for j in range(0, size-i-1):
        if(len(letterh[j])>len(letterh[j+1])):
            #swap these values
            letterh[j], letterh[j+1] = letterh[j+1], letterh[j]
    #print(letterh)
#outside the loops print the arrays
print(letterh)
    
"""
print("Hello, your name please")
name = input()
print("Hi", name, ", you are going to practice the lettera. When you have typed as much words as you want that start with the letter you are going to choose, you type done and the words will be put into a list. Have fun!")

print("Which letter?")
letter = input()


words = []

word = ""


for i in range(0,10):
    word = input("Enter word")
    while(word[0] not in [letter]):
        word = input("Wrong letter. Please reinput")    
    
    words.append(word)

print(words)
size = len(words)

for i in range(0, size):
    # make an inner loop that goes from 0 until len-i
    for j in range(0, size-i-1):
        if(len(words[j])>len(words[j+1])):
            #swap these values
            words[j], words[j+1] = words[j+1], words[j]
    #print(letterh)
#outside the loops print the arrays
print(words)