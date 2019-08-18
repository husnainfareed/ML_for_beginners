import matplotlib.animation as animation
import matplotlib.pyplot as plt
import csv
from matplotlib import style


# 9. Live Plot
plt.style.use('fivethirtyeight')

fig1 = plt.figure()

ax1 = fig1.add_subplot(1, 1, 1)


def animate(p):
    plot_data = open('sample.csv', 'r').read()

    line_data = plot_data.split('\n')
    x1 = []
    y1 = []

    for line in line_data:
        if len(line) > 1:
            x, y = line.split(',')
            x1.append(x)
            y1.append(y)

        ax1.clear()
        ax1.plot(x1, y1)


anime_data = animation.FuncAnimation(fig1, animate, interval=500)
plt.show()
