#List comprehension
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
#This is a simple for loop, declare item in list

cats = ['Princess', 'orange', 'Bob']
for cat in cats:
    print(cat.title() + ", that was a great catch!")

print("This is a text outside of the loop.")

#Be wary of the indentation.

#Numerical lists: range()

for value in range(1,5):
    print(value)
    #This prints 1-4. (X,Y-1)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
#Number from 1 and 10, with 2 steps (even)
print(even_numbers)
#Number from 1-10 with 2 steps (odd)
odd_numbers = list(range(1,11,2))
print(odd_numbers)

#List of first sq numbers
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares) #prints list!
print(square) #prints last item of list!

#More concisely,
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#Statistics

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#List comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
#Even numbers
squares1 = [value**2 for value in range(2,11,2)]
print(squares1)

#Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #Slicing is more faithful with numbers
print(players[1:4])
#this is the same as 0:4
print(players[:4])
#this is the same as 2:-1
print(players[2:])
#this is the same as [-3:-1]
print(players[-3:])

#Looping through slice
players =  ['charles', 'martina', 'michael', 'florence', 'eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #entire original list
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#Tuple
dimensions = (200 , 50)
print(dimensions[0]) #1st element
print(dimensions[1]) #2nd element

#tuple is a non changing list.
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#PEP8 style
#https://peps.python.org/pep-0008/

