import random

print("\n\n\t GUESSING GAME")
correct_number = random.randint(1,100)
if(correct_number % 2 == 0):
    type = "even"
else:
    type = "odd"

for count in range(1,6):
    num = int(input("\nGuess a number(1-100): "))
    
    if(num < 1 or num > 100):
        print("Invalid entery. Enter a number from 1-100", type)
    
    else:
        if(num == correct_number):
            print("\nCongratulations you won!\n\n")
            break
        
        else:
            if(count == 5):
                print("\nGame Over! You have exceeded your maximum trials (The correct number is",correct_number,")")
                print("\tThank you for playing this Game\n\n")
            else:
                print("Sorry you didnt get the correct number. You have", (5-count),"trials remaining")
                if(correct_number > num):
                    print("Hint: The correct number is an", type, "number Higher than", num)
                else:
                    print("Hint: The correct number is an", type, "number Lower than", num)
                    
        
        