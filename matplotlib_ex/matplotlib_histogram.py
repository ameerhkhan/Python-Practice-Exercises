import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

ages = [18, 19, 21, 21, 22, 22, 25, 26, 27, 28, 29, 30, 30, 31, 31, 55, 40, 19, 29, 30, 39]

bins = [10, 20, 30, 40, 50, 60] # will create 5 bins, 10-20, 20-30, 30-40, 40-50, 50-60
# data = pd.read_csv('data.csv')
# ids = data['Responder_id']
# ages = data['Age']

median_age = 29
color = '#fc4f30'


plt.hist(ages,                          # x-axis
         bins=bins,                     # divisions
         edgecolor='black',
         label='Ages of Respondents',   # edge color of each bin.
         histtype='barstacked',         # bar, barstacked, step, stepfilled.
         color='navy')

# draw a vertical line through the data.
plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.show()

