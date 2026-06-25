'''
7-1. Rental Car: Write a program that asks the user what kind of rental car they 
would like . Print a message about that car, such as “Let me see if I can find you 
a Subaru .”
'''

'''
car = input('What kind of rental car would you like? ')
print(f'Let me see if I can find you a {car}')
'''

'''
7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group . If the answer is more than eight, print a message say
ing they’ll have to wait for a table . Otherwise, report that their table is ready 
'''

'''
people = input(' how many people are in their dinner group: ')

people = int(people)

if people > 8:
    print(f'You will have to wait for a table')

else:
    print('Your table is ready')
'''


'''
Ask the user for a number, and then report whether the 
number is a multiple of 10 or not 
'''

'''
number = int(input('Enter a number: '))

if number % 10 == 0:
    print(f'{number} is a multiple of 10')
else:
    print(f'{number} is not a number multiple of 10')

'''


'''
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value . As they enter each topping, 
print a message saying you’ll add that topping to their pizza 
'''


'''
prompt = '\nEnter your pizza toppings'
prompt += '\n(Enter "quit" when you are done: )'

while True:
    message = input(prompt)

    if message == 'quit':
        break

    print(f'The {message.upper()} is added to your pizza')

'''

'''
while True:
    age = input("Enter your age (or type 'quit' to exit): ")

    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

'''

'''

print('----------new code------------')


7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari
ous sandwiches . Then make an empty list called finished_sandwiches . Loop 
through the list of sandwich orders and print a message for each order, such 
as I made your tuna sandwich. As each sandwich is made, move it to the list 
of finished sandwiches . After all the sandwiches have been made, print a 
message listing each sandwich that was made 


sandwich_orders = ['Bread_Sandwich','hotdog','cheeseburger','pizza']

finished_sandwiches = []

while sandwich_orders:
    current_sandwhich = sandwich_orders.pop()

    print(f'\n I made you a {current_sandwhich.title()} ')
    finished_sandwiches.append(current_sandwhich)



    print('\nlist of each sandwich that was made ')
    for finished_sandwiche  in finished_sandwiches :
       

     print(finished_sandwiche.title())
'''


'''
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
the sandwich 'pastrami' appears in the list at least three times . Add code 
near the beginning of your program to print a message saying the deli has 
run out of pastrami, and then use a while loop to remove all occurrences of 
'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
in finished_sandwiches 
'''

'''
sandwich_orders = ['hotdog','cheeseburger','pizza','pastrami','pastrami','pastrami']


print('\nthe deli has run out of pastrami')

while 'pastrami' in sandwich_orders:
    finished_pastrami = sandwich_orders.pop()
    print(f'\n{finished_pastrami} is out of menu')


print('\nUpdated Menu')
for sand in sandwich_orders:
    print(sand)
'''

'''
sandwich_orders = ['hotdog','cheeseburger','pizza','pastrami','pastrami','pastrami']


print('\nthe deli has run out of pastrami')

while 'pastrami' in sandwich_orders:
    finished_pastrami = sandwich_orders.pop()
    print(f'\n{finished_pastrami} is out of menu')


print('\nUpdated Menu')
for sand in sandwich_orders:
    print(sand)
'''

'''
7-10. Dream Vacation: Write a program that polls users about their dream 
vacation . Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll 
'''


D_Vacation = {}

while True:
    user = input('What is your name? ')
    vacation = input('What is your dream vacation? ')

    D_Vacation[user] = vacation

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        break

for user , vacation in D_Vacation.items():
    print(f'{user} would like to visit {vacation}')


    








