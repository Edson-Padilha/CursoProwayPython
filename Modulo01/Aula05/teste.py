import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')
plt.title('proway')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=4.0)

ax.set(xlim=(0, 10), xticks=np.arange(1, 8),
       ylim=(0, 10), yticks=np.arange(1, 8))



plt.show()