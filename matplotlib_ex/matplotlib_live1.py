import matplotlib.pyplot as plt
import pandas as pd

import random
from itertools import count
from matplotlib.animation import FuncAnimation

import csv

# x values could be dates or something.

plt.style.use('dark_background')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('Q:/Hamza/Python/Python_new_exercises/matplotlib_ex/data.csv')
    x = data['x_val']
    y1 = data['tot_1']
    y2 = data['tot_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1', color='red')
    plt.plot(x, y2, label='Channel 2', color='green')

    plt.legend(loc='upper left')
    #plt.tight_layout()

ani = FuncAnimation(plt.gcf(),
                    animate,
                    interval=1000)

plt.show()