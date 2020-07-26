import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn')

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 5, 5, 3, 6, 3, 6]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 7]
color = [7, 5, 3, 1, 2, 3, 4, 6, 8, 7, 8, 1, 0, 4, 4, 9]

sizes = [200, 100, 200, 300, 310, 201, 100, 99, 50, 209, 222, 350, 420, 99, 150, 400]
plt.scatter(x, y,
            s = 100, # size
            c = 'navy', # color
            marker = 'X', # marker
            edgecolors='black', # edgecolor
            linewidths=1, # size of edge
            alpha = 0.75 # soften the color
)

# can also use colormaps.


plt.scatter(y, x,
            s = sizes, # can define multiple sizes for each individual dot or cross
            c = color,
            cmap = 'Greens', # different colored dots, based on intensity in this case 1 - 10
            marker = 'X',
            edgecolors='black',
            linewidths=1,
            alpha=0.75
            )

cbar = plt.colorbar() # legen for what different color shades represent.
cbar.set_label('Satisfaction')
plt.show()