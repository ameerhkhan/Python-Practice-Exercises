#renaming files

import os

os.chdir('Q:/Hamza/Python/Python_new_exercises/automation')
print(os.getcwd())

i = 1

for f in os.listdir():
    #print(os.path.splitext(f)) # gives a tuple with the format (filename, extension)
    file_name, file_ext = os.path.splitext(f)
    # print(file_name)
    # print(file_ext)
    f_name = str(i)
    f_ext = file_ext
    new_name = '{}{}'.format(f_name, f_ext)
    #print(new_name)
    os.rename(f, new_name)
    i += 1

    # f_title, f_course, f_num = file_name.split('-') #split based on separation via '-'

    # print('{}-{}-{}{}'.format(f_num, f_course, f_title, file_ext))

    # pad single digits with zero for numbered lists.

    # f_num = f_num.strip()[1:].zfill(2)  #zfill used to fill up numbers to desired length. 2 equals 00, 3 --> 000
    # converts from ['#1 ' --> '01']

### PEWDIEPIE WOW!! ###
