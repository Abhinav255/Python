# Write python program that swap two number with temp variable and without temp variable
print("with temp")
a=int(input('enter number : '))
b=int(input('enter number : '))
c = a  # swapping the values of variables

print("before swapping with temp", "a=", a, ", b=", b)
a=b
b=c
print ("after swapping with temp","a=", a," ,b=" , b)

#swapping without temporary value
print("witout temp")
x=int(input('enter number : '))
y=int(input('enter number : '))
print("before swapping with temp", "x=", x, ", y=", y)

x=x+y
y=x-y
x=x-y
print("after swapping with temp", "x=", x, ", y=", y)
5
