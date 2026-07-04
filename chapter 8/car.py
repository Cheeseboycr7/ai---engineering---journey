from function import car_info

'''
8-16. Imports: Using a program you wrote that has one function in it, store that 
function in a separate file . Import the function into your main program file, and 
call the function using each of these approaches:
import module_name
'''

car = car_info('Camry','Toyota',color= 'blue', available = True)
print(car)