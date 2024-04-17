# 1 What is File function in python? What is keywords to create and write file. 

k="file function in python is simply very useful which led to allow user to handle files . read or write in any file and also perform many function in the file so it was also used as an storage type"

print(k)
# file=open("python.txt","x")
# file=open("python.txt","w")

# Opening a module3.1.txt file in write mode ("w")
file = open("python.txt", "w")
# Writing content to the file
file.write("Python is very easy to use and understanding Language\n")
# Closing the file to release system resources
file.close()