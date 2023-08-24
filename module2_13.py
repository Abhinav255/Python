#Write a Python program to count the number of characters (character frequency) in a string

c= input("enter any string")
s = []
for i  in c:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print(s)             