import numpy as np
import matplotlib.pyplot as plt

r = np.arange(1, 6, 1)
theta = [i * np.pi/2 for i in range(5)]
ax = plt.subplot(111, projection = 'polar')
ax.plot(theta, r, linewidth = 1, color = 'red')
ax.grid(True)
plt.show()