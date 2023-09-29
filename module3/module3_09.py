# Write a Python function that takes two lists and returns true if they have at least one common member. 

li1=[30,40,88,6,45,79,8]
li2=[34,44,88,60,5,97,9]


for i in li1:
    if i in li2:
        print("True")
    else:
        print("false")    