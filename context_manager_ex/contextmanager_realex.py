from contextlib import contextmanager
import os

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd() #get current working directory.
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd) #this is our final step whatsoever also called teardown when we teardown our work when completed.
    


with change_dir('Sample-Dir-one'):
    print(os.listdir())

with change_dir('Sample-Dir-two'):
    print(os.listdir())

#Useful for performing repetitive tasks to manage our resources efficiently.

