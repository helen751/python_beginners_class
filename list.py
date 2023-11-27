fruits = ["Mango", "Orange", "Apple", "Banana", "Cashew"]
print(fruits[2])
print(fruits[3])
print(fruits[1])
fruits[1] = "Watermelon"
#deleting an item in a list
del fruits[1]
print(fruits[1])

print(fruits[1:4])
print(fruits[1:-1])

#sublist
sea_fruits = ["coconut", "Kernel", "strawberry"]
fruits[1:4] = sea_fruits
print(fruits)

fruits.insert(1, "pineapple")
fruits.sort()
print(fruits)
fruits.sort(key=str.lower)
print ("list after sort : ", fruits)

#getting each element of a list using the for loop
#or fruit in fruits:
   # print(fruit)

lovely_fruits = fruits.copy()
print(lovely_fruits + fruits)