#Basics of Logging
#How to get started with Logging
#set different logging levels
#log INFO to files.

import logging

#logging levels allow us to specify exactly what we want to log by separating them into categories.
#Five standard logging levels
#Debug, Info, Warning, Error and Critical

#Details in Python Documentation

#Debug --> Detailed Information typically of interest when diagnosing problems
#Info --> Confirmation of proper working of a program
#Warning --> Indication of some problem or unexpected problems
#Error --> Serious problem hindering execution of a function
#Critical --> Serious error indicating the program itself maybe unable to continue running.

#By default, level is set to Warning or above.
#

#Setting basic LEVEL of Logging, Use to display on console.
logging.basicConfig(filename = 'test1.log', level = logging.DEBUG, 
            format = '%(asctime)s;%(levelname)s\t\t%(message)s') #format which the file will follow when logging.



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def square(x):
    return x**2



num_1 = 20
num_2 = 10

add_res = add(num_1, num_2)
# s('{} + {} = {}'.format(num_1, num_2, add_res)) #replace print with,
logging.debug('{} + {} = {}'.format(num_1, num_2, add_res)) 


subtract_res = subtract(num_1, num_2)
# print('{} - {} = {}'.format(num_1, num_2, subtract_res))
logging.warning('{} - {} = {}'.format(num_1, num_2, subtract_res))


multi_res = multiply(num_1, num_2)
# print('{} x {} = {}'.format(num_1, num_2, multi_res))
logging.debug('{} x {} = {}'.format(num_1, num_2, multi_res))

div_res = divide(num_1, num_2)
logging.debug('{} / {} = {}'.format(num_1, num_2, div_res))


sq_res = square(num_1)
logging.critical('{} * 2 = {}'.format(num_1, sq_res))