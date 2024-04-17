#  11 Write a Python program to write a list to a file.
# we have a list  which have the string
l=["Python is very easy and useful Language and very important to use "]
# we get the whole data into a variable
for j in l:
# print The Data
     print(j)
    
# Open the file "python.txt" in write mode ("a")s
file=open("harsh.txt","w")
# writing the File
file.write(j)
# closing The File
file.close
# Open the file "python.txt" in read mode ("r")
file=open("harsh.txt","r")
# now read and printing the lines 
print(file.readlines())
# closing the Files
file.close()