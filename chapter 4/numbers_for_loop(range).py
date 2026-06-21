'''
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
inclusive 
'''

'''
for value in range(1,21):
    print(value)
'''

'''
4-4. One Million: Make a list of the numbers from one to one million, and then 
use a for loop to print the numbers . (If the output is taking too long, stop it by 
pressing ctrl-C or by closing the output window .)
'''

'''
for value in range(1000001):
    million.append(value)
#print(million)
print('\n minimum value')
print(min(million))
print('\n mix value')
print(max(million))
print('\n sum of values')
print(sum(million))
million = []
'''

'''
4-6. Odd Numbers: Use the third argument of the range() function to make a list 
of the odd numbers from 1 to 20 . Use a for loop to print each number 
'''
odd_numbers =list(range(1,20,2))
#print(odd_numbers)


'''
4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to 
print the numbers in your list 
'''

multiple_0f_3 = [value*3 for value in range(1,31)]
#print('Multiples of 3')
#print(multiple_0f_3)

'''
4-8. Cubes: A number raised to the third power is called a cube . For example, 
the cube of 2 is written as 2**3 in Python . Make a list of the first 10 cubes (that 
is, the cube of each integer from 1 through 10), and use a for loop to print out 
the value of each cube 
'''
cubes_0f_3 = [value**3 for value in range(1,10)]  #list comprehension
#print('Cubes of 3')
#print(cubes_0f_3)


'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several 
lines to the end of the program that do the following:
•	Print the message, The first three items in the list are: . Then use a slice to 
print the first three items from that program’s list .
•	Print the message, Three items from the middle of the list are: . Use a slice 
to print three items from the middle of the list .
•	Print the message, The last three items in the list are: . Use a slice to print 
the last three items in the list 
'''

cars = ['BMW','Ferari','Toyota','Hilux','Honda']
first_3_items = cars[:3]
print('\nThe first three items in the list are')
print(f'{first_3_items} ')
print('\n--------------------')
midle_item = cars[1:4]
print('\nThree items from the middle of the list are')
print(f'{midle_item}')
print('\n---------------------')
last_3_item = cars[-3:]
print('\nThe last three items in the list are')
print(f'{last_3_item}')
print('\n---------------------')


'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
(page 60) . Make a copy of the list of pizzas, and call it friend_pizzas . 
Then, do the following:
•	Add a new pizza to the original list .
•	Add a different pizza to the list friend_pizzas .
•	Prove that you have two separate lists . Print the message, My favorite 
pizzas are:, and then use a for loop to print the first list . Print the message, 
My friend’s favorite pizzas are:, and then use a for loop to print the sec
ond list . Make sure each new pizza is stored in the appropriate list
'''

pizzas = ['meaty','cheese','veg']
friend_pizzas = pizzas[:]

pizzas.append('Something_Meaty')
print(pizzas)
friend_pizzas.append('pepperoni_pizza')

print(friend_pizzas)

for friend_pizza in friend_pizzas:
    print('\n My friend’s favorite pizzas are:')
    print(friend_pizza.title())

