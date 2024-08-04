cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Conditional tests
car = 'bmw'
print(car == 'bmw') #checking if true
print(car != 'audi') #checking if it's not true
print(car == 'audi') #checking if true

#Ignoring case - .lower(); .title()

#Multiple conditions:
#condition AND condition
#(age_0 >= 21) and (age_1 >= 21)
#(age_0 >= 21) or (age_1 >= 21)
#Checking if true can be used with 'in'
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#Boolean expressions - assign boolean to values
game_active = True
can_edit = False

#If statements
#do something if condition = True
age = 19
if age >= 18:
    print("You are old enough to vote!")

#If else blocks
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#If-elif-else chain

age = 12
if age < 4:
    price = 0
    print("Your admission cost is $0.")
elif age < 18:
    price = 5
    print("Your admission cost is $5.")
else:
    price = 10
    print("Your admission cost is $10.")

print("Your admission cost is $" + str(price) + ".")

#Multiple conditions: if-elif-..-elif-else
#But else is not required. if-elif-...-elif will do.


