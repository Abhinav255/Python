# 6 Write a Python program to read a file line by line and store it into a list
# Open the file "python.txt" in append mode ("r")
file =open("python.txt","r")
# taking a "h" blank list
h=[]
# now start a loop which can store all the data in j variable
for j in file:
    # now we append all the data in h name list which created
    h.append(j)
    # print the list 
print(h)
# closing the file
file.close()