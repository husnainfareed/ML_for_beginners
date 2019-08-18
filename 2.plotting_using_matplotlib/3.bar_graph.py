
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 24, 36, 40, 5]

tick_label = ['One', 'Two', 'Three', 'Four', 'Five']

plt.bar(x, y, tick_label=tick_label, width=0.7,
        color=['green', 'orange', 'blue'])

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Graph')
plt.show()
