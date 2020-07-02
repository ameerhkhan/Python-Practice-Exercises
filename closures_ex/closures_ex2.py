import logging

logging.basicConfig(filename='example_closure.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return(log_func)



def add(x, y):
    return(x+y)

def sub(x, y):
    return(x-y)

def mul(x, y):
    return(x*y)

add_logger = logger(add)
sub_logger = logger(sub)
mul_logger = logger(mul)

add_logger(4, 5)
sub_logger(9, 5)
mul_logger(4, 5)

#These closures can be extremely powerful.