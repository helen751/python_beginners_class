#finding the mean median and mode of numbers

print("\n\n\tSTATISTICS APPLICATION")
numbers = []

for x in range(5):
    number = int(input("Please enter the No"+str(x+1)+": "))
    numbers.insert(x, number)

numbers.sort()    
print("\nNumbers =", numbers)
mean = sum(numbers) / len(numbers)

print("Mean =", mean)

if(len(numbers)%2 == 1):
    78,79,80,67
    i = int((len(numbers)/2)+0.5)-1
    median = numbers[i]
    print("Median =", median)
    
else:
    i = int((len(number)/2) + ((len(number)/2)-1)) / 2
    median = numbers[i]
    print("Median =", median)
    




    

           