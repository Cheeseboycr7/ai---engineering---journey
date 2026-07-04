'''
10-1. Learning Python: Open a blank file in your text editor and write a few 
lines summarizing what you’ve learned about Python so far . Start each line 
with the phrase In Python you can... . Save the file as learning_python.txt in the 
same directory as your exercises from this chapter . Write a program that reads 
the file and prints what you wrote three times . Print the contents once by read
ing in the entire file, once by looping over the file object, and once by storing 
the lines in a list and then working with them outside the with block 
'''

filename ='chapter 10/learning_python.txt'

'''
with open(filename) as file_object:
    contents = file_object.readlines()

for i in range(3):
    print(contents)
'''


'''
with open(filename) as file_object: # first open the file 
    contents = file_object.readlines() # read from the file 


p_string = '' # create the variable to contain the content from the file read
for content in contents:  # loop through the file and add to the the p_string variable
    p_string += content.lstrip()

print(f'\n{p_string}')
print(len(p_string)) # find the lent of the content

'''


'''
with open(filename) as file_object: # first open the file 
    contents = file_object.readlines() # read from the file 


p_string = '' # create the variable to contain the content from the file read
for content in contents:  # loop through the file and add to the the p_string variable
    p_string += content.lstrip()
    p_string.replace('python', 'Java')

p_string = p_string.replace("python", "Java")
print(p_string)

'''



'''
10-3. Guest: Write a program that prompts the user for their name . When they 
respond, write their name to a file called guest.txt 
'''

'''
filename = 'chapter 10/guest.txt'

name = input("What is your name? ")
with open(filename, 'a') as file_object:
  file_object.write(f'{name}\n')
'''



'''
10-4. Guest Book: Write a while loop that prompts users for their name . When 
they enter their name, print a greeting to the screen and add a line recording 
their visit in a file called guest_book.txt . Make sure each entry appears on a 
new line in the file 
'''

'''
filename = 'chapter 10/guest_book.txt'

while True:
    name = input("What is your name? (type 'quit' to exit) ")
    if name.lower() == 'quit' or 'quit' in name.lower():
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f'{name}\n')
        print(f"Hello, {name}! Your name has been added to the guest book.")
'''


filename = 'chapter 10/responses.txt'

while True:
    responses = input('Why do you like or enjoy programming? (type "quit" to exit) ')
    if responses.lower() == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f'{responses}\n')
        print(f'Thank you for participating in the survay, your response\n has been added to the response text file'.lstrip())






