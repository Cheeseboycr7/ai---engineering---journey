## String formating

name = 'mandla'.strip().title()
fav_color = 'black'.title()
hobby = 'playing games'.lower()
fav_dish = 'beef stew'.title()


card = (
    "My favourate things\n"
    "--------------------\n"

    f"Name: \t {name}\n"
    f"favourate Color: {fav_color}\n"
    f"hobby: {hobby} \n"
    f"favourate dish: {fav_dish}"
)

#print(card)

## Challege 2

name = input("What your name?:").strip().title() 
favorite_book = input("Enter your favorite book:").upper()
favorite_color = input("What is your favorite color?").strip().title()
Dream_job = input("Enter your dream job:").title()

message = (
    "My profile\n"
    "---------------------\n"

    f'Name: \t {name}\n'
    f'favorite_book: \t {favorite_book}\n'
    f'favorite_color: \t {favorite_color}\n'
    f'Dream_job: \t {Dream_job}\n'
)

print(message)