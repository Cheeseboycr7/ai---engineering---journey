'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
not empty .
•	If the list is empty, print the message We need to find some users!
•	Remove all of the usernames from your list, and make sure the correct 
message is printed 
'''

'''
usernames = []
if usernames:  # Check if the list is not empty
    for username in usernames: # Loop through the list of usernames and assign each username to the variable username
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')
else:
    print('We need to find some users!')
'''


'''
5-10. Checking Usernames: Do the following to create a program that simulates 
how websites ensure that everyone has a unique username .
•	Make a list of five or more usernames called current_users .
•	Make another list of five usernames called new_users . Make sure one or 
two of the new usernames are also in the current_users list .
•	Loop through the new_users list to see if each new username has already 
been used . If it has, print a message that the person will need to enter a 
new username . If a username has not been used, print a message saying 
that the username is available .
•	Make sure your comparison is case insensitive . If 'John' has been used, 
'JOHN' should not be accepted 
'''

current_users = ['admin','eric','john','michael','sarah','Cheeseboy']
new_users = ['employee','eric','john','Technician']


for new_user in new_users: # Loop through the new_users list and assign each username to the variable new_user
    if new_user in current_users:
        print(f'The username {new_user} is already taken. Please enter a new username.')
    else:
        print(f'The username {new_user} is available.')



'''
'''

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')


