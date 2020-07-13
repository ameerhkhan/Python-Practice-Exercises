import matplotlib.pyplot as plt
import random
import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

# x_vals = [x for x in range(10)]
# y_vals = [y**2 for y in range(10)]

x_vals = []
y_vals = []

#counts up one number at a time.
index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 10))

    plt.cla()

    plt.plot(x_vals, y_vals)

ani = FuncAnimation(plt.gcf(),      # get current figure
                    animate,        # function that you want plot
                    interval=1000)  # time between next iteration.




plt.tight_layout()
plt.show()