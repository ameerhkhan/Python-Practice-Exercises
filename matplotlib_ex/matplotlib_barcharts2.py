import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv # standard library but pandas is faster at reading csv files.
from collections import Counter # will be used to count how many times each language appears in a list.

#creating bar charts to determine most popular programming languages.

plt.style.use('dark_background')

# old and outdated and slow method of reading csvs.
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)   # generated a dictionary object that contains the data present in the csv based on the index.
    language_count = Counter()

    row = next(csv_reader)
    print(row['LanguagesWorkedWith'].split(';'))
    for row in csv_reader:
        language_count.update(row['LanguagesWorkedWith'].split(';'))

print(language_count.most_common(15)) # returns a list of top 15 languages.
# Each element in the list is a tuple which contains the name of the language and its count. ('Python', 281881)

languages = []
popularity = []

for item in language_count.most_common(15): # can also use zip.
    languages.append(item[0]) # item will be the tuple and 0, 1 define the language and count respectively.
    popularity.append(item[1])

# plt.bar(languages, popularity) # vertical method.
languages.reverse()
popularity.reverse() # comment these out and find what difference they make for a much clearer explanation.
plt.barh(popularity, languages) # horizontal method. Good for a large number of values.

plt.title('Most Popular Languages')
# plt.xlabel('Languages')
plt.xlabel('No of Users')

plt.show()
