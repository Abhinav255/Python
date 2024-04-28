# Write a python program to sum of the first n positive integers

n = int(input("Enter number: "))  
sum=0
for i in range (1,n):
    if i%2==0:
        sum+=i
        
print(sum)    