'''
10-11. Favorite Number: Write a program that prompts for the user’s favorite 
number . Use json.dump() to store this number in a file . Write a separate pro
gram that reads in this value and prints the message, “I know your favorite 
number! It’s _____ .”
'''

import json
from json import JSONDecodeError


def store_favourite_num():
    favourite_num = input("What is your favourite number? ")

    with open("favourite_num.json", "w") as f:
        json.dump(favourite_num, f)

    return favourite_num


def get_stored_favourite_num():
    try:
        with open("favourite_num.json") as f:
            favourite_num = json.load(f)
            return favourite_num

    except (FileNotFoundError, JSONDecodeError):
        return None


def get_user_info():
    favourite_num = get_stored_favourite_num()

    if favourite_num:
        print(f"I know your favourite number! It's {favourite_num}.")
    else:
        favourite_num = store_favourite_num()
        print(f"I'll remember that your favourite number is {favourite_num}.")


#get_user_info()