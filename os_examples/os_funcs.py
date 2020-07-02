import os
from datetime import datetime

# Allows us to interact with the underlying operating system in several different ways.
# Following are a few of the things we can do with it.

#print(dir(os))

print(os.getcwd()) # --> get cuurent working directory


os.chdir('q:/Hamza/Python/Python_new_exercises/os_examples') # --> change CWD
os.mkdir('OS-Demo-2')                 # -->  cannot make subirectories/ deeper directories.
#os.makedirs('OS-Demo-2/Sub-Dir-1')    # -->  makes subdirectories even when top-level directory is not made.

os.rmdir('OS-Demo-2')                 # --> removes directories.
#os.removedirs('OS-Demo-2/Sub-Dir-1')  # --> similar working as to makedirs.

os.rename('test.txt', 'demo.txt')     # --> renames files.

print(os.stat('demo.txt'))              # --> print information about the directory.
mod_time = os.stat('demo.txt').st_mtime # --> gets you last modified time.
print(datetime.fromtimestamp(mod_time)) # --> Human readable form.

os.walk(os.getcwd())           # --> generator that yields a tuple of three values as it is walking the directory tree.

# Let's look at an example.

# By default top down walk.

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

    # extremely useful for finding required files. or ones with required extension?

# We can get environment variables
# prints(os.environ.get('HOME')) # --> get environment variables for Home directory.

# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')    # --> gives us the correct/ proper path.
file_path = os.path.join(os.getcwd(), 'test.txt')
print(file_path)

# create new file,
with open(file_path, 'a') as f:
    f.write('Something.')

print(os.path.basename('/tmp/test.txt'))  # --> grab the filename that exists on any path we are working name
print(os.path.dirname('/tmp/test.txt'))   # --> grab the path.
print(os.path.split('/tmp/test.txt'))     # --> gives a list of directory and file.

print(os.path.exists('/tmp/test.txt'))    # --> Does the path exist?
print(os.path.isdir('/tmp/test.txt'))     # --> is it a dir?
print(os.path.isfile('/tmp/test.txt'))    # --> is it a file?

print(os.path.splitext('/tmp/test.txt'))  # --> It will split the file root and the extension. As used before. in automation

print(dir(os.path))


print(os.getcwd())

print(os.listdir()) # --> List files in CWD

