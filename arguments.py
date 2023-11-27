
def addition(a, b=8, c = 67):
    result = a+b
    return result

#keyword argument    
print(addition(a = 12, c = 5))
#positional Argument
print(addition(34,5))


#local and global variables
name = "helen"
def welcome():
    name = "Grace"
    print("Welcome",name)
    
welcome()
print(name)