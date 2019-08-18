
import matplotlib.pyplot as plt

# 6. Pie Chart
activities = ['eat', 'sleep', 'work', 'play']

slices = [3, 7, 8, 6]

colors = ['r', 'g', 'm', 'b']

plt.pie(slices, labels=activities, colors=colors, startangle=90,
        shadow=True, explode=(0.2, 0, 0, 0), autopct='%1.2f%%')

plt.legend()
plt.show()
