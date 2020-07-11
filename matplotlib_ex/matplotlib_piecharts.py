import matplotlib.pyplot as plt

plt.style.use('dark_background')

#slices of a pie
slices = [10, 40, 20, 30]
labels = ['Ten', 'Fourty', 'Twenty', 'Thirty']
colors = ['blue', 'red', 'yellow', 'purple'] #can also use hex values.

colors_hex = ['#008fd5', '#fc4f30', '#e5ae37', '#6d9045']


plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'}, colors=colors_hex)



plt.title('A Generic Pie Chart')
plt.tight_layout() #default padding which looks really nice.
plt.show()