import os

os.chdir('Q:/Hamza/Python/Python_new_exercises/file_objects')

cwd = os.getcwd()

print(cwd)
#file_path = os.path.join(cwd, 'test.txt')

# r --> read, w--> write, a --> append i.e edit file from last cursor
with open('test2.txt', 'a') as f: # --> use W to write to a file. Also overwrites any file with the same name so be careful
    f.write('Test\n')               # --> write to the file.
    # f.seek(0)
    f.write('Back at the start!\n') # --> overwrote! Don't use that much!
    
