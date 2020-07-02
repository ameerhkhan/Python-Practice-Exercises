#some people use classes as decorators instead of function
#let's have a look at that.

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print('Call method executed this before {}.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
    
@decorator_class
def display():
    print('Display Function Ran!')

display()


@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', '23')

@decorator_class
def display_more(name, age, gender):
    print('More information --> ({} {} {})'.format(name, age, gender))

display_more('John', '50', 'Male')