'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you 
create to 10 . If you want to try more comparisons, write more tests and add 
them to conditional_tests.py . Have at least one True and one False result for 
each of the following:
•	Tests for equality and inequality with strings
•	Tests using the lower() function
•	Numerical tests involving equality and inequality, greater than and 
less than, greater than or equal to, and less than or equal to
•	Tests using the and keyword and the or keyword
•	Test whether an item is in a list
•	Test whether an item is not in a list
'''

car = 'bmw'
#print(car.upper() == 'BMW')

food = ['cake','orange','banana','pizza']

# check if cake is in the list using the in function
avalable = 'cake' in food
#print(avalable)

vanilla_cake = 'cake'
#food.remove('cake')


if vanilla_cake == 'cake' in food or vanilla_cake == "banana" in food:
   print(f'{vanilla_cake} is avalable in the menu you can order one')

else:
    
    print(f'{vanilla_cake} is not avalable from the menu')


print("\n------------------New LINE of Code--------------------------")

'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game . Create a 
variable called alien_color and assign it a value of 'green', 'yellow', or 'red' .
•	Write an if statement to test whether the alien’s color is green . If it is, print 
a message that the player just earned 5 points .
•	Write one version of this program that passes the if test and another that 
fails . (The version that fails will have no output .)
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
write an if-else chain .
•	If the alien’s color is green, print a statement that the player just earned 
5 points for shooting the alien .
•	If the alien’s color isn’t green, print a statement that the player just earned 
10 points .
•	Write one version of this program that runs the if block and another that 
runs the else block 
'''








   # print("\n------------------New LINE of Code--------------------------")















alien = ['green','red','yellow','black']

if 'red' in alien:
    print('player earned 5 point')

if 'red' in alien:
    print('player earned 10 point')

if 'red' in alien:
    print('player earned 15 point')

    


'''
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
stage of life . Set a value for the variable age, and then:
•	If the person is less than 2 years old, print a message that the person is 
a baby .
•	If the person is at least 2 years old but less than 4, print a message that 
the person is a toddler .
•	If the person is at least 4 years old but less than 13, print a message that 
the person is a kid .
•	If the person is at least 13 years old but less than 20, print a message that 
the person is a teenager .
•	If the person is at least 20 years old but less than 65, print a message that 
the person is an adult .
•	If the person is age 65 or older, print a message that the person is an 
elderly .
'''

def stage_of_life(age):
    if age < 2:
        print('the person is a baby')

    elif age >= 2 and age < 4:
        print('the person is a toddler')

    elif age >= 4 and age < 13:
        print('the person is a kid')

    elif age >= 13 and age < 20:
        print('the person is a teenager')

    elif age >= 20 and age < 65:
        print('the person is an adult')

    else:
        print('the person is an elderly')


print("\n------------------New LINE of Code--------------------------")
stage_of_life(1)
stage_of_life(3)
stage_of_life(10)       
stage_of_life(15)
stage_of_life(30)   



'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
independent if statements that check for certain fruits in your list .
•	Make a list of your three favorite fruits and call it favorite_fruits .
•	Write five if statements . Each should check whether a certain kind of fruit 
is in your list . If the fruit is in your list, the if block should print a statement, 
such as You really like bananas!
'''

print("\n------------------New LINE of Code--------------------------")

favorite_fruits = ['banana','orange','grape']

for fruit in favorite_fruits:
    if fruit == 'banana':
        print('You really like bananas!')

    if fruit == 'orange':
        print('You really like orange!')

    if fruit == 'grape':
        print('You really like grape!')




'''
5-8. Hello Admin: Make a list of five or more usernames, including the name 
'admin' . Imagine you are writing code that will print a greeting to each user 
after they log in to a website . Loop through the list, and print a greeting to 
each user:
•	If the username is 'admin', print a special greeting, such as Hello admin, 
would you like to see a status report?
•	Otherwise, print a generic greeting, such as Hello Eric, thank you for log
ging in again.
'''

print("\n------------------New LINE of Code--------------------------")

usernames = ['admin','eric','john','michael','sarah','Cheeseboy']

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')

    elif username == 'eric':
        print('Hello Eric, thank you for logging in again.')

    elif username == 'john':
        print('Hello John, thank you for logging in again.') 

    elif username == 'michael':
        print('Hello Michael, thank you for logging in again.')

    elif username == 'sarah':
        print('Hello Sarah, thank you for logging in again.')

    elif username != 'Cheeseboy':
        print('Hello Cheeseboy, thank you for logging in again.')

    else:
        print('Try to register an account')
        


