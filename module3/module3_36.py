#   How Do You Check The Presence Of A Key In A Dictionary?
def checkKey(dic, key):
    if key in dic.keys():
        print("Present, ", end =" ")
        print("value =", dic[key])
    else:
        print("Not present")
         
# Driver Code
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)
 
# key = 'w'
# checkKey(dic, key)