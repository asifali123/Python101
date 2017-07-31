import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [6, 8, 11, 7, 9]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'k']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct="%1.1f%%"
        )

plt.legend()
plt.show()
