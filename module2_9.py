#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
a = int(input("Enter the first integer: "))
b=int (input ("Enter second integer:"))
c=int (input ("Enter third integer"))

if a==b or b==c or c==a:
    print("Sum is zero")
else:
    print('sum is',a+b+c)