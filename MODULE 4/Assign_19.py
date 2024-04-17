# 19 How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets. 
# this are answer of the above theory question
k="Now Firstly Try Execute then it will go to Except And it will Throw The Message which is there in except and also Finally Will also gets Executed Because It will always Execute often There is a error or not"
print(k)
# this are answer of the above theory question in practical form
# try statement of  exceptional handling
try:
    v="there Is an easy solution"
    print(v)
# except statement of exceptional handling if try fail then except occur
except:
    print(NameError,ValueError,KeyError)
# finally  statement of  exceptional handling which always get executed  
finally:
    print("This is Exceptional handling")
