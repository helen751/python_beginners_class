
def greeting():
    print("Welcome everyone. hope you are good!")
    print("God bless you")

def goodbye():
    print("Goodbye to you. I love you")
    
print("\n\nHELLO WORLD")
msg = input("Do you want a Welcome message or a goodbye message: ")

if(msg.lower() == "welcome"):
    greeting()
    
elif(msg.lower() == "goodbye"):
    goodbye()
    
else:
    print("Always follow instructions")