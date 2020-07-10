# pip install matplotlib

from matplotlib import pyplot as plt

print(plt.style.available) # --> available styles.

#HOW DO YOU USE A STYLE?
plt.style.use('dark_background')

# ages from 25 to 35
dev_x = [x for x in range(25, 36)]
py_dev_x = [x for x in range(25, 36)]

# can be replaced with, 
ages_x = [x for x in range(25, 36)]


#median salaries for above ages.
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57827, 60316, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

#plt.plot(x, y)
plt.plot(ages_x, dev_y, 'r--', label ='All Devs', linewidth=3)

plt.plot(ages_x, py_dev_y, color='b', linestyle=':', marker='.', label='Python', linewidth=4, markersize=3)

#can also use HEX color values.
plt.plot(ages_x, js_dev_y, color='#adad3b', linestyle='-.', label='JavaScript', linewidth=4)

plt.title('Median Salary (USD) by age.')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')


plt.legend()

plt.grid(True) # --> to show the grid.

plt.tight_layout() # --> to stop cutting of our data on the plot.
# plt.legend(['All Devs', 'Python']) # list # replaced with labels in above code.
plt.show()
