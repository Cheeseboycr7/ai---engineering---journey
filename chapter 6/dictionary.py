'''
6-1. Person: Use a dictionary to store information about a person you know . 
Store their first name, last name, age, and the city in which they live . You 
should have keys such as first_name, last_name, age, and city . Print each 
piece of information stored in your dictionary 
'''

'''
persons = {
    "first_name" : "Mandla",
    "last_name" : "Shezi",
    "age" : 30,
    "Country" : "South Africa"
}
print('\nMy Profile')
print("----------")

for person in persons:
    if person == "first_name":
        print(f"My first name is {persons[person].title()}")

    elif person == "last_name":
        print(f"My last name is {persons[person].title()}")

    elif person == "age":
        print(f"My age is {persons[person]}")

    elif person == "Country":
        print(f"I live in {persons[person].title()}")


print("Thank you for taking the time to read my profile!")
print("--------------New Code------------------")

'''
'''
favourite_numbers = {
    "Ronaldo" : 7,
    "Messi" : 10,
    "Mbappe" : 9,
    "bellingham" : 22,
    "yamal" : 18
}

for fav in favourite_numbers:
    print(f"\n{fav.title()} favourite jersey number is {favourite_numbers[fav]}")


print('\nThe greatest footballer of all time is Ronaldo')
'''


'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary . 
However, to avoid confusion, let’s call it a glossary .
•	Think of five programming words you’ve learned about in the previous 
chapters . Use these words as the keys in your glossary, and store their 
meanings as values .
•	Print each word and its meaning as neatly formatted output . You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line . Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output
'''



glossary = {
    "string" : "A series of characters",
    "integer" : "A whole number",
    "float" : "A number with a decimal point",
    "boolean" : "A data type that can only have two values: True or False",
    "list" : "A collection of items that are ordered and changeable",
}

'''
for term in glossary:
    print(f"\n{term.title()} : {glossary[term]}")

print("\nThank you for taking the time to read my glossary!")
'''


'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
up the code from Exercise 6-3 (page 102) by replacing your series of print 
statements with a loop that runs through the dictionary’s keys and values . 
When you’re sure that your loop works, add five more Python terms to your 
glossary . When you run your program again, these new words and meanings 
should automatically be included in the output 
'''

'''
for key , value in glossary.items():
    print(f"\n{key.title()} : {value}")
'''

'''
'''

famous_rivers = {
    "nile" : "egypt",
    "amazon" : "brazil",
    "yangtze" : "china",
    "mississippi" : "united states",
    "ganges" : "india",
    "Manzana" : "Eswatini"
}

'''
for river , country in famous_rivers.items():
    print(f"\nThe {river.title()} river runs through {country.title()}")
'''

'''
for river in famous_rivers.keys():
    print(f"\n{river.title()} is a famous river")
'''

'''
for country in famous_rivers.values():
    print(f"\n{country.title()} is a country with a famous river")
'''

'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people_to_poll = ['jen', 'moses', 'edward', 'james', 'phil']

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"\nThank you for taking the poll {person.title()}")
    else:
        print(f"\n{person.title()} please take the poll")

'''

'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102) . 
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people . Loop through your list of people . As you 
loop through the list, print everything you know about each person 
'''


users = {
    "Mandla" : {
        "first_name" : "Mandla",
        "last_name" : "Shezi",
        "age" : 30,
        "Country" : "South Africa"
    },

    "Sibongile" : {
        "first_name" : "Sibongile",
        "last_name" : "Shezi",
        "age" : 28,
        "Country" : "South Africa"
    },

    "Thandi" : {
        "first_name" : "Thandi",    
        "last_name" : "Shezi",
        "age" : 25,
        "Country" : "South Africa"
    }
}

for username , user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    age = user_info['age']
    country = user_info['Country']

    print(f"Full Name: {full_name}")
    print(f"Age: {age}")
    print(f"Country: {country}")



print('--------------New Code------------------')


'''
6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
name of a pet . In each dictionary, include the kind of animal and the owner’s 
name . Store these dictionaries in a list called pets . Next, loop through your list 
and as you do print everything you know about each pet
'''

pets = {
    "dog" : {
        "name" : "Buddy",
        "age" : 3,
        "breed" : "Golden Retriever",
        "owner" : "John"
},

    "cat" : {
        "name" : "Whiskers",
        "age" : 2,
        "breed" : "Siamese",
        "owner" : "Emily"
    },

    "parrot" : {
        "name" : "Polly",
        "age" : 1,
        "breed" : "African Grey",
        "owner" : "Michael"
    }

}

for animal_type, animal_info in pets.items():
    print(f"\nAnimal Type: {animal_type.title()}")
    name = animal_info['name']
    age = animal_info['age']
    breed = animal_info['breed']
    owner = animal_info['owner']

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Breed: {breed}")
    print(f"Owner: {owner}")


'''
6-9. Favorite Places: Make a dictionary called favorite_places . Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person . To make this exercise a bit more interesting, ask some friends 
to name a few of their favorite places . Loop through the dictionary, and print 
each person’s name and their favorite places 
'''

print('\n--------------New Code------------------')

favorite_places = {
        "mandla" : {
            "places" : ["south africa", "zimbabwe", "kenya"]
        },
        "sibongile" : {
            "places" : ["south africa", "zimbabwe", "kenya"]
        },
        "thandi" : {
            "places" : ["south africa", "zimbabwe", "kenya"]
        }
}

for name, places_info in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places_info['places']:
        print(f"- {place.title()}") 


'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
each person can have more than one favorite number . Then print each person’s 
name along with their favorite numbers 
'''

print('\n--------------New Code------------------')

fourate_numbers ={
    "Mandla" : {
        "favourite_number" : [7, 10, 9]
    },
    "Sibongile" : {
        "favourite_number" : [3, 8, 15]
    },
    "Thandi" : {
        "favourite_number" : [5, 12, 20]
    }
}

for name, number_info in fourate_numbers.items():
    print(f"\n{name.title()}'s favourite numbers are:")
    for number in number_info['favourite_number']:
        print(f"- {number}")


print('--------------NEW CODE---------------')

'''
6-11. Cities: Make a dictionary called cities . Use the names of three cities as 
keys in your dictionary . Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city . The keys for each city’s dictionary should be something like 
country, population, and fact . Print the name of each city and all of the infor
mation you have stored about it 
'''


cities = {
    "new york" : {
        "country" : "united states",
        "population" : 8419600,
        "fact" : "New York City is known as the 'Big Apple'."
    },
    "tokyo" : {
        "country" : "japan",
        "population" : 13929286,
        "fact" : "Tokyo is the most populous metropolitan area in the world."
    },
    "paris" : {
        "country" : "france",
        "population" : 2140526,
        "fact" : "Paris is known as the 'City of Light'."
    }
}

for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\nCity: {city.title()}")
    print(f"Country: {country.title()}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")
