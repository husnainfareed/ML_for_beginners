

import matplotlib.pyplot as plt
import numpy as np
import csv

# 8. Data from csv file
x = []
y = []

with open('sample.csv') as csvfile:
    plots = csv.reader(csvfile)
    for col in plots:
        x.append(col[0])
        y.append(col[1])

plt.plot(x, y, label='File')
plt.xlabel('x-label')
plt.ylabel('y-label')

plt.title('Test Graph')
plt.legend()
plt.show()
