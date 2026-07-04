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