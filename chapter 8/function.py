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

while True:
    print("(enter 'q' at any time to quit)")
    
    artist = input('Enter the artist name: ')
    if artist  == 'q':
        break

    album = input('Enter the abum name associated with the artist you provided: ')
    if artist  == 'q':
        break

    result = make_album(artist, album)
    print(result)
