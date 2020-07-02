import os

os.chdir('Q:/Hamza/Python/Python_new_exercises/file_objects')

cwd = os.getcwd()

# In order to read pictures we have to use binary mode by changing,
# 'r' with 'rb'
# 'w' with 'wb'

with open('1.jpg', 'rb') as rf:
    with open('2_copy.png', 'wb') as wf:
        # for line in rf:
        #     wf.write(line)

        #instead of doing it line by line. we will do chunk size.
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
        