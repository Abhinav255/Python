# Explain Inheritance in Python with an example? What is init? Or What 
# Is A Constructor In Python? 

k="inheritance Is Simply A heirarchy of class or Simply called realtion Between the Classes Or Simply The Concept of Heritance Ex you grandfather have propertt so it will give you to your father and after That it will given to you so this will also happens in the classes"
print(k)
# creating class of grandfather
class grandfather:
    # creating a function
    def func(self):
        # printing The String
        print(" More land")
# creating class of father and inheritate grandfather
class father(grandfather):
    # creating a function
    def func2(self):
        # printing The String
        print("More Money")
# creating class of son and inheritate father and grandfather    
class Son(father,grandfather):
    # creating a function
    def Func3(self):
        # printing The String
        print("more Power")

# now creating a object of son because in son the father and grandfather inheritated
obj=Son()
# object called by .operator
obj.func()
obj.func2()
obj.Func3()
print()

# this are answer of the above theory question
j="the Init is Simply A constructor Means It will execute When The Object is Created "
print(j)

l="The Constructor is Simply When there is a website started or at the start When The object Is Created it will started or executed "
print(l)