import matplotlib.pyplot as plt

#Use Piechart for comparing 5 to 6 items. Anymore than that will render the comparison hard to read.

plt.style.use('dark_background')

slices = [59219, 55466, 47544, 36443, 35917, 7201]

labels = ['Javasript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Go']

explode = [0,0,0,0.2,0,0] #to emphasize on a slice of Pie. 0.1 --> how much explosion?

plt.pie(slices, labels=labels, 
            wedgeprops={'edgecolor':'#ffffff'}, # colorize edges of each slice.s
            explode=explode, # emphasize
            shadow=True,  # Shadow
            startangle=90, # rotate the chart according to desired orientation.
            autopct='%1.1f%%' # to show percentages.
            )

plt.title('Programming languages Popularity')

plt.tight_layout()

plt.show()
