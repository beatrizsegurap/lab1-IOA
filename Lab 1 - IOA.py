import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f(x,y):
    return (0.3*x + 0.52*y)



'''
f(x,y) = 0,3x + 0,52y
restricciones:
X>=0
Y >= 0
2,5x+y >= 3                     ->  y = 3-2,5x
'''


x_vals = np.linspace(0, 800, 10) # 10 valores entre 0 y 800
f1 = (3 - 2.5*x_vals) # y = 3-2,5x
plt.figure(figsize=(10,8))
plt.plot(x_vals, f1, label=r'$x_1 + 1.5x_2 \leq 750$') 
plt.plot(375, 250, 'b*', markersize=15)

# Región factible
y3 = np.minimum(f1, f2)
plt.fill_between(x_vals, 0, y3, alpha=0.15, color='b')
plt.axis(ymin = 0)
plt.title('Optimización lineal')
plt.legend()
plt.show()