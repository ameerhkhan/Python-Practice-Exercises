import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

ages_x = [x for x in range(25, 36)]

x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57827, 60316, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes - width, dev_y, color='red', label='All Devs', width=width)
plt.bar(x_indexes, py_dev_y, color='blue', label='Python Devs', width=width)
plt.bar(x_indexes + width, js_dev_y, color='green', label='JS Devs', width=width)


plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x) # for using proper required indexes.

plt.title('Median Salary USD by age')
plt.xlabel('Ages')
plt.ylabel('Salaries')

plt.show()