#  4 Write a Python program to read first n lines of a file.
# Get the number of lines to read from user input
n = int(input("enter The lines you read : "))
# Open the file "python.txt" in append mode ("r")
file = open("python.txt", "r")
# Read and print the specified number of lines from the file
for i in range(n):
    # read And print the lines 
    print(file.readline(), end="")
# closing The File
file.close()