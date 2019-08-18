
import matplotlib.pyplot as plt
import numpy as np

# 7. Plot Merging
x = np.arange(0, 2*np.pi, 0.01)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='Sin')
plt.plot(x, y2, label='Cos')

plt.xlabel('x-label')
plt.ylabel('y-label')
plt.title('Sin and Cosine Functions')

plt.legend()
plt.show()
