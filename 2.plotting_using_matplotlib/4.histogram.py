

import matplotlib.pyplot as plt

# # 4. Histogram Plot
ages = [2, 56, 96, 14, 78, 23, 65, 21, 45, 82, 41, 23,
        65, 98, 74, 85, 11, 25, 99, 41, 25, 36, 14, 25]

range = (0, 100)
bins = 10

plt.hist(ages, bins, range, color='green', histtype='bar', rwidth=0.7)

plt.xlabel('Ages')
plt.ylabel('Bins')
plt.title('Histogram Plot')
plt.show()
