from StoreData import *

def verify_user_info():
    favourite_num = get_stored_favourite_num()

    if favourite_num:
        answer = input(f"I know your favourite number! It's {favourite_num}. Is that correct? (yes/no) ")

        if answer.lower() == 'yes':
            print("Great! I'm glad I remembered correctly.")
        else:
            favourite_num = store_favourite_num()
            print(f"I'll remember that your favourite number is {favourite_num}.")


verify_user_info()