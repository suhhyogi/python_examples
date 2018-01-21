import numpy as np
import matplotlib.pylab as plt
'''
x = y
1   1
2   2
0.5 0.5
'''
def x2(value1):
    return np.array(value1 > 2, dtype=int)

x = np.arange(-5, 5, 0.1)
y = x2(x)

print(y)

plt.plot(x, y)
plt.grid()
plt.show()