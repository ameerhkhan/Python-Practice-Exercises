#Dynamically Alter the Functionality of your functions.


# def outer_function(msg):
#     #message = msg #can also pass this variable to inner function without assigning a var to it in the outerfunction

#     def inner_function():
#         print(msg) #The inner function has access to variables in the outer function. Also called free variables
#     return(inner_function) #this returns the function without executing. and waits for execution. Assign a variable.


#outer_function()
#my_func = outer_function()
#my_func()   #This is called a closure. Remembers our message variable even after our outer_function has already been executed.
#my_func()

# hi_func = outer_function('hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()

#Above was a brief summary of closures.
#NOW let's move on to decorators.
#Decorator takes another function as an argument. Adds somekind of functionality and returns
#another function without altering the source code of the original function used.


def decorator_function(original_function): #giving a function as an argument makes this a simple decorator.
    def wrapper_function(*args, **kwargs):
        print('Wrapper function executed this before, {}'.format(original_function.__name__))
        return original_function(*args, **kwargs) #if paranthesis not used, function will not run.
    return wrapper_function

@decorator_function #Use this to forego below code which passes display as argument.
def display():
    print('Display function ran')

#Forego this code with  
# decorated_display = decorator_function(display)

# decorated_display()
# hi_func = decorator_function('hi')
# bye_func = decorator_function('Bye')

##
#With this^
display()


#Why use decorators?
#Decorating our functions allows us to easily add more functionality to our existing function by adding
#that functionality inside of our wrapper. i.e. We haven't modified the display function.

#Let's make another original function,

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', '23')

#But to pass in arguments into wrapper function we have to put in *args, **kwargs
#Which signifies passing any number of arguments or keyword arguments into our original function.

#What if we use three arguments?

@decorator_function
def display_more(name, age, gender):
    print('More information --> ({} {} {})'.format(name, age, gender))

display_more('John', '50', 'Male')

#So two arguments to show any number of arguments??
#YES!! WOOHOO!!