#Logging is one of the most common uses of decorators.
#let's find out the amount of time our functions run, and the arguments it generated.

from functools import wraps #to maintain original functionality of our functions. READ NEXT LINE.

#Basically so that logging file is not wrapper (which was done automatically by our program) 
# but instead it should be named what we intend to name i.e. for this instance display_info.log


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO) #log file matching name of our original function.
    #logging.INFO --> logs that we ran the function and also log the arguments.

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args,kwargs)
        )
        return(orig_func(*args, **kwargs))
    
    return wrapper


def my_timer(orig_func):
    import time
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return(result)
    return wrapper

import time

# @my_timer
# def display():
#     time.sleep(2)
#     print('display function ran!')


#We can use the below code. to update our log.

#basically sends the following function into above function as ORIGINAL FUNCTION
#so enhance its abilities there. Without ruining this function.
@my_logger
@my_timer 
def display_info(name, age, t):
    time.sleep(2)
    print('Display_info ran with arguments ({}, {} {})'.format(name, age, t))

#display()
t = time.time()
display_info('Mughal', '29', t)

#how to apply both above decorators on function?
#Order matters when applying more than 1 decorator to a function. same as,
#display_info = my_logger(my_timer(display_func))

#Hence we can see why position is important.








# def decorator_function(original_function): 
#     def wrapper_function(*args, **kwargs):
#         print('Wrapper function executed this before, {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs) 
#     return wrapper_function


# @decorator_function 
# def display():
#     print('Display function ran')

# display()

# @decorator_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('John', '23')

# @decorator_function
# def display_more(name, age, gender):
#     print('More information --> ({} {} {})'.format(name, age, gender))

# display_more('John', '50', 'Male')

