import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

import numpy as np

# we can replace the dict reader with the pandas library.

data = pd.read_csv('data_csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for responses in lang_responses:
    language_counter.update(responses['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(popularity, languages)

plt.title('Most Popular Languages')

plt.xlabel('No of Users')

plt.show()

