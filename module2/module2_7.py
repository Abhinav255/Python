#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

num1 = int(input("enter 1st number: "))


if num1%2==0:
    print("{} is even".format(num1))
else:
    print("{} is odd".format(num1))  