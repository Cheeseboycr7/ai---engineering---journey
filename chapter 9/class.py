'''
9-1. Restaurant: Make a class called Restaurant . The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type . 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indi
cating that the restaurant is open .
Make an instance called restaurant from your class . Print the two attri
butes individually, and then call both methods 
'''
'''

class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):

        print(f'This {self.restaurant_name.title()} serve this type of cuisine: {self.cuisine_type.title()}')

    def  open_restaurant(self):

        self.is_open = True
        print(f'{self.restaurant_name.title()} is open')
'''


        
#food_shop = Restaurant('Nandos','Grilled_Chicken')
#food_shop.describe_restaurant()
#food_shop.open_restaurant()

'''
9-2. Three Restaurants: Start with your class from Exercise 9-1 . Create three 
different instances from the class, and call describe_restaurant() for each 
instance 
'''

#grocery = Restaurant('Pick n Pay','Quality food') # create instances
#grocery.describe_restaurant()
#grocery.open_restaurant()




'''
9-3. Users: Make a class called User . Create two attributes called first_name 
and last_name, and then create several other attributes that are typically stored 
in a user profile . Make a method called describe_user() that prints a summary 
of the user’s information . Make another method called greet_user() that prints 
a personalized greeting to the user .
Create several instances representing different users, and call both methods 
for each user
'''


class User():

    def __init__(self, first_name, last_name, *more_info):

        self.first_name = first_name
        self.last_name = last_name
        self.more_info = more_info


    def describe_user(self):
        print(f'\nMy name is {self.first_name} {self.last_name}')


        if self.more_info:
            print('More infomation about me')
            for info in self.more_info:
                print(info)

    
    def greet_user(self):
        print(f'hello {self.first_name} welcome to python class hope you enjoy')


#user1 = User('Mandla','Shezi', 27, 'Male', 'Computer Science Student')
#user1.describe_user()
#user1.greet_user()



'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166) . 
Add an attribute called number_served with a default value of 0 . Create an 
instance called restaurant from this class . Print the number of customers the 
restaurant has served, and then change this value and print it again .
Add a method called set_number_served() that lets you set the number 
of customers that have been served . Call this method with a new number and 
print the value again .
Add a method called increment_number_served() that lets you increment 
the number of customers who’ve been served . Call this method with any num
ber you like that could represent how many customers were served in, say, a 
day of business
'''



class Restaurant():

    def __init__(self,restaurant_name,cuisine_type ):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
       


    def describe_restaurant(self):

        print(f'\nThis {self.restaurant_name.title()} serve this type of cuisine: {self.cuisine_type.title()}')

    def  open_restaurant(self):

        self.is_open = True
        print(f'{self.restaurant_name.title()} is open')


    def numbers_served(self):
       
        print(f'The number served is ' + str(self.number_served))


    def set_number_served(self,number):

        self.number = number
        print(f'The number served is {number}')


    def increment_number_served(self, increament_number):

        self.number += increament_number
        print(f'The number of customers served is {self.number}')


'''
restuarent = Restaurant('KFC','Chicken')
restuarent.describe_restaurant()
restuarent.number_served = 9  # change the attribute directly from the method
restuarent.numbers_served()  # call the metod
restuarent.set_number_served(10)
restuarent.increment_number_served(20)
'''


'''
9-5. Login Attempts: Add an attribute called login_attempts to your User 
class from Exercise 9-3 (page 166) . Write a method called increment_
login_attempts() that increments the value of login_attempts by 1 . Write 
another method called reset_login_attempts() that resets the value of login_
attempts to 0 .
Make an instance of the User class and call increment_login_attempts() 
several times . Print the value of login_attempts to make sure it was incremented 
properly, and then call reset_login_attempts() . Print login_attempts again to 
make sure it was reset to 0 
'''



'''
class User():

    def __init__(self, first_name, last_name, *more_info):

        self.first_name = first_name
        self.last_name = last_name
        self.more_info = more_info
        self.login_attempts = 0


    def describe_user(self):
        print(f'\nMy name is {self.first_name} {self.last_name}')


        if self.more_info:
            print('More infomation about me')
            for info in self.more_info:
                print(info)

    def greet_user(self):
        print(f'hello {self.first_name} welcome to python class hope you enjoy')


    def increment_login_attempts(self):

        self.login_attempts += 1
        print(f'{self.first_name} your number of login attempt is {self.login_attempts}')

    def reset_login_attempts(self):

        self.login_attempts = 0
        print(f'{self.first_name} your login attempt is resseted {self.login_attempts}')



user1 = User('Mandla','Shezi', 27, 'Male', 'Computer Science Student')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.increment_login_attempts()
'''


'''
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant . Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of 
the class will work; just pick the one you like better . Add an attribute called 
flavors that stores a list of ice cream flavors . Write a method that displays 
these flavors . Create an instance of IceCreamStand, and call this method 
'''


'''
class IceCreamStand(Restaurant):

     def __init__(self,restaurant_name,cuisine_type):
         
         super().__init__(restaurant_name,cuisine_type)

     def displayflavours(self, *flavours):

         self.flavours = flavours
         print('Available Icecream flavours')
         for flv in self.flavours:
             print(flv)


ice = IceCreamStand('KFC','Icecream')
ice.displayflavours('Vanilla','Chocolate','Strawberry')
'''




'''
9-7. Admin: An administrator is a special kind of user . Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on . 
Write a method called show_privileges() that lists the administrator’s set of 
privileges . Create an instance of Admin, and call your method
'''

'''
9-8. Privileges: Write a separate Privileges class . The class should have one 
attribute, privileges, that stores a list of strings as described in Exercise 9-7 . 
Move the show_privileges() method to this class . Make a Privileges instance 
as an attribute in the Admin class . Create a new instance of Admin and use your 
method to show its privileges
'''
class Privileges():

 def __init__(self):
  
     self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]
  
 def show_privilages(self):

        print('List of privilages for Admin')
        for pr in self.privileges:
            print(pr)


class Admin(User):

    def __init__(self, first_name, last_name, *more_info):
        super().__init__(first_name, last_name, *more_info)

        self.privileges = Privileges() # Instances as Attributes

ad = Admin('Mandla','Shezi')
ad.privileges.show_privilages()  # calling Instances as Attributes






    




         
         
    

         






