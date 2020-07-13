import matplotlib.pyplot as plt

# plt.style.use('fivethirtyeight')
plt.style.use('dark_background')
#plt.xkcd()


minutes = [x for x in range(1, 10)] # minutes

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]   # point per minute
player2 = [1, 1, 1, 1, 1, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['Player1', 'Player2', 'Player3']
colors = ['green', 'red', 'purple']
#plt.pie([1, 1, 1], labels=['PLayer1,', 'Player2', 'Player3']) # [1, 1, 1] --> score for first minute hardcoded.

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.title('General Stack Plot')
plt.tight_layout()

plt.legend(loc='upper left') # can also pass a tuple containing the co-ordinates.


plt.show()

