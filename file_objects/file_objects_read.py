# Interacting with file objects

# f = open('Q:/Hamza/Python/Python_new_exercises/file_objects/test.txt', 'r')

# print(f.name) # --> name of the file.
# print(f.mode) # --> mode -> read/write
# print(f.readline()) # --> print line by line.
# print(f.readline)

# f.close()

# Now using context manager to open the file which is the proper way of opening a file and automatically closes the file
# closing the file is absolutely necessary.
import os

os.chdir('Q:/Hamza/Python/Python_new_exercises/file_objects')
print(os.getcwd())
cwd = os.getcwd()
file_path = os.path.join(cwd, 'test.txt')
# print(file_path.replace('\\','/'))

# file_p = file_path.replace('\\', '/')
# file_n = file_p.replace('q', 'Q')


with open(file_path, 'r') as f:
    # f_contents = f.read()
    # print(f_contents)
    # f_lines = f.readlines() # --> presents all of the lines in the list.
    # print(f_lines)
    # f_line = f.readline() # reads one line and moves onto the next.
    # print(f_line, end='')

    # Instead of writing readline for all of the lines. use a For loop

    # for line in f:
    #     print(line, end='') # end = '' --> signifies what you want to do at the end of each line.
    size_to_read = 100
    f_content = f.read(4) # --> reads 4 characters at a single instance and remembers the pointer.
    # while len(f_content) > 0:
        
    #     print(f_content, end = '')
    #     f_content = f.read(4)
    #     print(f.tell()) # --> where's the cursor.

    print(f_content, end=' ')
    f.seek(0) # --> sets the cursor to desired position.
    
    f_content = f.read(4)
    print(f_content)

    


