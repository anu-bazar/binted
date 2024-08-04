#BASIC SYNTAX


#LISTS
#Def: collection of items in particular order
#Syntax: name = ['arg1', 'arg2', ...]

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#Accessing elements
#Starts numbering from 0
print(bicycles[0]) 
print(bicycles[0].title()) #Capitalized
print(bicycles[1]) #second item
print(bicycles[3]) #fourth item

print(bicycles[-1]) #last element
print(bicycles[-3]) #third from the end
print(bicycles[-4]) #fourth from the end
#Using individual value from list
message = "My first bike was a " + bicycles[0].title() + "."
print(message)

names = ['Alice', 'Noor', 'Shay']
print(names[0])
print(names[2])

message1 = "I met my friend " + names[1] + " on a Groupon cruise."
print(message1)

transportation = ['car', 'bus', 'motorcycle']
brand = ['Honda', 'Toyota', 'Mitsubishi']
message2 = "I want to own a " + brand[2] + " " + transportation[0] + "."
print(message2)

#Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding elements to list - add to end
motorcycles.append('ducati')
print(motorcycles)

#Inserting elements to list - add to xth
motorcycles.insert(0, 'bugatti')
print(motorcycles)

#Removing elements - remove xth
del motorcycles[0]
print(motorcycles)
#inaccessible after deleted

#Removing via pop()
#Used when you need to use the value of the item removed

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles) #stored removed item

motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#You can pop from xth index
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#Removing by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') #remove value
print(motorcycles)

#Remove can do pop() too kinda?
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#remove only deletes the first occurence. 

#List organization
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

