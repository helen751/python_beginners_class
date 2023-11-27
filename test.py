numbers = []

for x in range(4):
    num = int(input("Enter a number: "))  
    numbers.insert(x, num) 

average = sum(numbers) / len(numbers)
print("Sorted list:", numbers)
print("Average:", average)