#Closures:

# A closure is a record storing a function together with an environment.
# a mapping associating each free variable of the function with the value
# or storage location which the name was bound when the closure was created.

# A closure, unlike plain functions allows the function to access those captured variables
# through the closure's reference to them, even when the function is invoked outside their scope.

# In simple terms,
# A closure is an inner function that remembers/has access to variables in the local scope in which it 
# was created even when the outerfunction has finished executing.

# closure closes over free variables from their environment.

def outer_func(msg):
    message = msg # --> free reference variable.

    def inner_func():
        print(message + '\n')
        print('\n')
    
    def inner_arg(*args):
        print('{} {}'.format(msg, str(args).strip("()''")))

    return(inner_arg) # --> if you want to run a function use paranthesis!!!


jo_func = outer_func('Jo')
bo_func = outer_func('Bo')
# print(my_func.__name__)
jo_func('What?', 'This')
bo_func('Yo?')

