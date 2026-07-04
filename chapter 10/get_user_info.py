'''
10-12. Favorite Number Remembered: Combine the two programs from 
Exercise 10-11 into one file . If the number is already stored, report the favorite 
number to the user . If not, prompt for the user’s favorite number and store it in a 
file . Run the program twice to see that it works
'''
from StoreData import *

def get_user_info():
    favourite_num = get_stored_favourite_num()

    if favourite_num:
        print(f"I know your favourite number! It's {favourite_num}.")
    else:
        favourite_num = store_favourite_num()
        print(f"I'll remember that your favourite number is {favourite_num}.")


get_user_info()