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





    