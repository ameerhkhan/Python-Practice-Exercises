import matplotlib.pyplot as plt
# import pandas as pd

plt.style.use('seaborn')

# data = pd.read_csv('data.csv')

# ages = data['Age']
ages_x = [x for x in range(25, 36)]

# dev_salaries = data['All_devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']

dev_salaries = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_salaries = [45372, 48876, 53850, 57827, 60316, 65998, 70003, 70000, 71496, 75370, 83640]
js_salaries = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]



fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(ages_x, py_salaries, label='Python')
ax1.plot(ages_x, js_salaries, label='JavaScript')
ax2.plot(ages_x, dev_salaries, label='All Developers', color='#ff0110', linestyle='--')

#Use ALT to select and edit multiple contents.


ax1.legend()
ax1.set_title('Median Salary (USD) by age')
# ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')


ax2.legend()
#ax2.set_title('Median Salary (USD) by age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

# plt.legend()

# plt.title('Median Salary (USD) by age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')

plt.show()
fig.savefig('figure_subpng')
# plt.gca()
# plt.gcf()
