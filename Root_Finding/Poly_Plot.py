import numpy as np
import matplotlib.pyplot as plt

a = -3
b = 20
c = -20
d = -12
# e = 85
# f = -31
x = np.linspace(-20, 20, 265, endpoint=True)
y = (a * (x * x * x) + b * (x * x) + c * x + d)

plt.plot(x, y)

plt.grid(color='gray', linestyle='-')

axes = plt.gca()
axes.set_ylim([-5000, 5000])
axes.set_xlim([-10, 10])

plt.show()