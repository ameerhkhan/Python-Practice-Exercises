# help(plt.fill_between)
# Fill the area between two horizontal curves.

import matplotlib.pyplot as plt

plt.style.use('dark_background')

ages_x = [x for x in range(25, 36)]

dev_salaries = [38496, 42000, 46752, 49320, 70000, 70000, 72000, 64928, 67317, 68748, 73752]
py_salaries = [45372, 48876, 53850, 57827, 60316, 65998, 70003, 70000, 71496, 75370, 83640]
js_salaries = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

overall_median = 57827

plt.plot(ages_x, dev_salaries, color='#FF4400', linestyle='--', label='All Devs')

plt.plot(ages_x, py_salaries, label='Python', color='#FFFF44')

#fill the entire area under python plotted area,
plt.fill_between(ages_x,        # define x axis
                py_salaries,    # fill from y1
                dev_salaries, # y2 # to define passing point for above and below coloring.
                where=(py_salaries > dev_salaries), # color above this condition.
                interpolate=True,
                alpha = 0.5,
                color='purple',
                label='Above Average')    

plt.fill_between(ages_x,        
                py_salaries,   
                dev_salaries, 
                where=(py_salaries <= dev_salaries),
                interpolate=True,
                alpha = 0.5,
                color='red',
                label='Below Average')    

plt.legend()

plt.title('Median Salary (USD) by age')
plt.xlabel('Ages')
plt.ylabel('Median Salary')

plt.tight_layout()

plt.show()