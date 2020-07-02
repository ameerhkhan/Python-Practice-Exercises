import logging
import employee



#Since employee module got imported first, The level of Logging is set at INFO
#hence Debug is below that level and does not print.


# logging.basicConfig(filename = 'testnew.log', level = logging.DEBUG, 
#             format = '%(asctime)s;%(levelname)s\t\t%(name)s %(message)s')

#ROOT WILL SHOW UP because, since we haven't specified a specific logger we are working with the root logger
#best to specify loggers for each type of logging.

#hence best to use different logger for different programs so that sanity is maintained.
#so we can configure both separately

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s;%(levelname)s\t\t%(name)s %(message)s')

file_handler = logging.FileHandler('testbrandnew.log')
file_handler.setLevel(logging.ERROR) #to only log ERROR statements.
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        # logger.error('Tried to DIVIDE by ZERO')
        #can also use,
        logger.error('Tried to DIVIDE by ZERO')
    else:
        return 

def square(x):
    return x**2


num_1 = 20
num_2 = 0

add_res = add(num_1, num_2)
# s('{} + {} = {}'.format(num_1, num_2, add_res)) #replace print with,
logger.debug('{} + {} = {}'.format(num_1, num_2, add_res)) 


subtract_res = subtract(num_1, num_2)
# print('{} - {} = {}'.format(num_1, num_2, subtract_res))
logging.debug('{} - {} = {}'.format(num_1, num_2, subtract_res))


multi_res = multiply(num_1, num_2)
# print('{} x {} = {}'.format(num_1, num_2, multi_res))
logger.debug('{} x {} = {}'.format(num_1, num_2, multi_res))

div_res = divide(num_1, num_2)
logger.debug('{} / {} = {}'.format(num_1, num_2, div_res))


sq_res = square(num_1)
logging.critical('{} * 2 = {}'.format(num_1, sq_res))


#FOR MORE GOTO DOCUMENTATIONS.