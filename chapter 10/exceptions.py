'''
10-6. Addition: One common problem when prompting for numerical input 
occurs when people provide text instead of numbers . When you try to convert 
the input to an int, you’ll get a TypeError . Write a program that prompts for 
two numbers . Add them together and print the result . Catch the TypeError if 
either input value is not a number, and print a friendly error message . Test your 
program by entering two numbers and then by entering some text instead of a 
number
'''


'''
print('Enter two numbers and I will add them together.')

try:
    input1 = input('First number: ')
    input2 = input('Second number: ')   
    sum = int(input1) + int(input2)
    print(f'The sum of {input1} and {input2} is {sum}.')
except ValueError: # catch a ValueError if the input cannot be converted to an integer
    print('You must enter valid numbers and an integer number not decimal.')
'''

#print('Enter two numbers and I will add them together.')

'''
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop 
so the user can continue entering numbers even if they make a mistake and 
enter text instead of a number 
'''

'''
while True:
    try:
        input1 = input('First number: ')
        input2 = input('Second number: ')   
        sum = int(input1) + int(input2)
        print(f'The sum of {input1} and {input2} is {sum}.')
        break  # exit the loop if the inputs are valid
    except ValueError:  # catch a ValueError if the input cannot be converted to an integer
        print('You must enter valid numbers. Please try again.')

'''

from Dog_Cat import ReadFile

#rs = ReadFile('chapter 10/dogs.txt')
rs = ReadFile('chapter 10/cats.txt')
print(rs)