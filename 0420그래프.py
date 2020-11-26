import numpy as np
import matplotlib.pyplot as plt

# domain
a = 0
b = 6
N = 601
x = np.linspace(a, b, N)
y = np.zeros_like(x)

# main loop
for k in range(0, N):
    x_temp = x[k]
    if x_temp >= 0 and x_temp < 2:
        y[k] = x_temp**2 -2*x_temp + 2
    elif x_temp >= 2 and x_temp < 4:
        y[k] = -x_temp**2 + 6*x_temp - 8
    else:
        y[k] = x_temp**2 - 10*x_temp + 26
        

# visualize
plt.plot(x, y, '.')
plt.show()