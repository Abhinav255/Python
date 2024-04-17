# Write python program that user to enter only odd numbers, else will raise an exception
# take a user input from user 
h=int(input("Enter The Number : "))
# try block from exceptional handling
try:
    # now condition for odd Number
    if h%2!=0:
        # print the result
        print(h," is odd")
        # else statement 
    else:
        # print else condition
        print(v)
        # except block 
except:
    # error handling
    print(ValueError,NameError)