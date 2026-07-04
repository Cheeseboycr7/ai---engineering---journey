class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):

        print(f'This {self.restaurant_name.title()} serve this type of cuisine: {self.cuisine_type.title()}')

    def  open_restaurant(self):

        self.is_open = True
        print(f'{self.restaurant_name.title()} is open')


