from contextlib import contextmanager

#Sample way to write some text or doing something with a file

# f = open('test.txt', 'w')
# f.write('This is another test') #RE WRITES ANY EXISTING FILE.
# f.close()

#recommended way to do something with a file.
#In this case no need to close down the file even if an error occurs.
#This is called a Context manager
#can be used to handle databases automatically
#can acquire and release locks

#There's plenty of use cases for context managers.

# with open('test.txt', 'w') as f:
#     f.write('This is yet another test of Context Managers')


#We will create a context manager to open and then close a file.

#first we are going to use classes to use/make our context managers.

# class Open_File():

#     def __init__(self, filename, mode): #filename: name of file, mode: what to do with the file
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode) #open command from above shifted here
#         return(self.file) #returning file variable 

#     def __exit__(self, exc_type, exc_val, traceback):
#         #we wanna be sure our file closes when exit is executed
#         self.file.close()
#         #extra arguments to catch errors
        

# with Open_File('sample.txt', 'w') as f:
#     f.write('Testing') #f is now a file object on which we can use write/erase whatever.

# print(f.closed)



##############################################
#Now we are going to use a function to perform the above task
#We need contextlib module along with contextmanager decorator.

@contextmanager #this is a f*cking decorator
def open_file(my_file, mode):
    #to catch errors we may use try and finally. try will try to do what's asked of it
    #and even if that command fails to proceed, finally will close the file whatsover.
    try:
        f = open(my_file ,mode) #the enter method of class method.
        yield(f)
    finally:
        f.close()

with open_file('sample.txt', 'w') as f:
    f.write('Yet another sample \n \ttext file.')

print(f.closed)
