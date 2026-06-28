'''
8-1. Message: Write a function called display_message() that prints one sen
tence telling everyone what you are learning about in this chapter . Call the 
function, and make sure the message displays correctly 
'''

def display_message():
    print('You are learning fuctions in chapter 8')

#display_message()


'''
8-2. Favorite Book: Write a function called favorite_book() that accepts one 
parameter, title . The function should print a message, such as One of my 
favorite books is Alice in Wonderland . Call the function, making sure to 
include a book title as an argument in the function call 
'''

def favorite_book(title) :
    print(f'One of my favourate books is {title.title()}')

#favorite_book('python')


'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
text of a message that should be printed on the shirt . The function should print 
a sentence summarizing the size of the shirt and the message printed on it .
Call the function once using positional arguments to make a shirt . Call the 
function a second time using keyword arguments 
'''

def make_shirt(size, text):
    print(f'The size of the shirt is {size} and the message written is {text}')


# make_shirt('medium','"Python is the best programming language"') #using positional arguments
# make_shirt(size='medium', text='Hello world') # using keyword arguments 


'''
8-6. City Names: Write a function called city_country() that takes in the name 
of a city and its country . The function should return a string formatted like this:
"Santiago, Chile"
'''


def city_country(city , country):

    city_counrty = f'{city.title()} is the capital city of {country.title()}'
    return city_counrty


c_counrty = city_country('Mbabane','Eswatini')
#print(c_counrty)



'''
8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album . The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information . Use the function to make three dictionaries representing different 
albums . Print each return value to show that the dictionaries are storing the 
album information correctly 

Add an optional parameter to make_album() that allows you to store the 
number of tracks on an album . If the calling line includes a value for the num
ber of tracks, add that value to the album’s dictionary . Make at least one new 
function call that includes the number of tracks on an album 
'''

def make_album(artists , albums , tracks=''):

    person = {'artist': artists.title() , 'album': albums.upper()}

    if tracks:
        person['tracks'] = tracks

    return person



artist1 = make_album('Drake', 'Iceman', 20)
artist2 = make_album('Drake', 'HABIBTI')
artist3 = make_album('Drake', 'Her Loss')

#print(f'\n{artist1}')
#print(f'\n{artist2}')
#print(f'\n{artist3}')


'''
8-8. User Albums: Start with your program from Exercise 8-7 . Write a while 
loop that allows users to enter an album’s artist and title . Once you have that 
information, call make_album() with the user’s input and print the dictionary 
that’s created . Be sure to include a quit value in the while loop 
'''



'''
while True:
   # print("(enter 'q' at any time to quit)")
    
    artist = input('Enter the artist name: ')
    if artist  == 'q':
        break

    album = input('Enter the abum name associated with the artist you provided: ')
    if artist  == 'q':
        break

    result = make_album(artist, album)
    #print(result)
'''

'''
8-9. Magicians: Make a list of magician’s names . Pass the list to a function 
called show_magicians(), which prints the name of each magician in the list 
'''

def show_magicians(magicians):
    for magician in magicians:
        print(f'{magician}')


magicians = ['Chris','Ganda','Mandla','Cheeseboy']
#show_magicians(magicians)




'''
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9 . 
Write a function called make_great() that modifies the list of magicians by add
ing the phrase the Great to each magician’s name . Call show_magicians() to 
see that the list has actually been modified 
'''


def make_great(magicians):
      for magician in magicians:
        print(f'The great magician {magician}')


#make_great(magicians)

#show_magicians(magicians)



'''
8-11. Unchanged Magicians: Start with your work from Exercise 8-10 . Call the 
function make_great() with a copy of the list of magicians’ names . Because the 
original list will be unchanged, return the new list and store it in a separate list . 
Call show_magicians() with each list to show that you have one list of the origi
nal names and one list with the Great added to each magician’s name
'''

'''
print('-------NEW CODE-------')
new_magicians = magicians[:]
make_great(new_magicians) # make a copy of list magicians
show_magicians(magicians)
show_magicians(new_magicians)
'''


'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants 
on a sandwich . The function should have one parameter that collects as many 
items as the function call provides, and it should print a summary of the sand
wich that is being ordered . Call the function three times, using a different num
ber of arguments each time 
'''

def making_sandwich(*sandwiches):

    if sandwiches:
        print('\nSandwich ingridients: ')
        for sandwich in sandwiches:
            print(f'{sandwich}')


#making_sandwich("cheese")
#making_sandwich("cheese", "lettuce", "tomato")
#making_sandwich("cheese", "bacon", "polony", "egg", "mayonnaise")




'''
8-13. User Profile: Start with a copy of user_profile.py from page 153 . Build 
a profile of yourself by calling build_profile(), using your first and last names 
and three other key-value pairs that describe you 
'''

def user_profile(first,last, **info):

    profile = {'first_name': first , 'last_name':last}
   
    for key , value in info.items():
        profile[key] = value

    return profile


#user_profiles = user_profile('Mandla','Shezi', country = 'Eswatini', sex = 'male')

#print(user_profiles)


'''
8-14. Cars: Write a function that stores information about a car in a diction
ary . The function should always receive a manufacturer and a model name . It 
should then accept an arbitrary number of keyword arguments . Call the func
tion with the required information and two other name-value pairs, such as a 
color or an optional feature . Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
'''


def car_info(manufacture, model, **more_info):

    cars = {'manufacture': manufacture, 'model': model}

    for key , value in more_info.items():
        cars[key] = value

    return cars

car_inf = car_info('subaru','outback', color = 'blue' ,tow_package = True)
print(car_inf)



