print("\n\n\tVOTING SYSTEM")
name = input("Please Enter your Name: ")
age = int(input("How old are you: "))

if(age < 18):
    print("Sorry you are not Eligible to vote. Come back in the next", (18-age), "Years")
    
else:
    print("\n\tVote for your best candidate for President")
    print("1. Bola Ahmed Tinubu \n2. Peter Obi \n3. Atiku Abubakar")
    vote = int(input("\nPlease choose your candidate(1-3): "))
    
    if(vote < 1):
        print("Sorry you missed your chance to vote because you dont take instructions")
        
    elif(vote > 3):
        print("Sorry you missed your chance to vote because you dont take instructions")
    
    else:
        print("You have successfully voted for your best candidate")
        print("\n\nThank you for voting!")
        
    
