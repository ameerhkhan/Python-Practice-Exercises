import os

os.chdir('Q:/Hamza/Python/Python_new_exercises/file_objects')

cwd = os.getcwd()

with open('test.txt', 'r') as rf:       # --> open existing file
    with open('test_copy.txt', 'w') as wf:   # --> create a new file for copying.
        for line in rf:
            wf.write(line)              # --> copy new file.