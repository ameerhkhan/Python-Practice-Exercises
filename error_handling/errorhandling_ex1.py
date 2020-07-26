# If we can anticipate sections of our code that might throw an error we should make an attempt to handle such file.
# always have specific errors in the beginning and more general errors in the end of a try except blocks.
try:
    f = open('test_file.txt')

    # we can also raise exceptions on our own.
    if f.name == 'corrupt_file.txt':
        raise Exception             # or any other that one would like.

    # var = bad_var                 # --> this will also make an exception.
    # try to make specific exceptions for each type of error.
except FileNotFoundError as e:
    # print('Sorry this file doesn\'t exist')
    print(e)
except Exception as e:
    # print('Sorry, something went wrong.')
    print(e)
else:                               # only runs when there are no errors or exceptions.
    print(f.read())
    f.close()
finally:                            # runs whether there are error/exceptions or not.
    print('Finally ending this.')


