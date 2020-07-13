# Tracking contribution of users/students/developers in the completio  of the project.

import matplotlib.pyplot as plt
from random import randint as randd

plt.style.use('dark_background')

minutes = [x for x in range(1, 10)]

emp1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
emp2 = [0, 1, 1, 2, 2, 4, 4, 5, 7]
emp3 = [0, 1, 2, 1, 2, 2, 3, 2, 1]

# Above data is better for showing the use of stack plots.
# When one whole piece is broken into different parts per minute.

# emp2 = [randd(0,8) for x in range(1, 10)]
# emp3 = [randd(0,8) for x in range(1, 10)]
# print(emp1, emp2, emp3)

labels = ['Employee1', 'Employee2', 'Employee3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(minutes, # x axis.
            emp1, emp2, emp3, # y axis.
            labels=labels,
            colors=colors)

plt.legend(loc=(0.07, 0.05))

plt.title('Contribution Towards a Project')
plt.tight_layout()
#plt.figure(figsize=(20, 10))

plt.show()


