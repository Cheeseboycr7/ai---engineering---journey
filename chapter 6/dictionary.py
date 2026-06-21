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



