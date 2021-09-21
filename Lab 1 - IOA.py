import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


'''
def f(x,y):
    return (0.3*x + 0.52*y)

f(x,y) = 0,3x + 0,52y -> y= -0.3x/0.52
restricciones:
X>=0
Y >= 0
2,5x+y >= 3         ->  y = 3-2,5x
x+2y >=4            ->  y = (4-x)/2


def objetivo(y3, yOBJ, minmax): #y3 curva maxima/minima, yOBJ=f objetivo, minmax = busca maximizar(1) o minimizar(0)
    puntos = y3[0]
    pendiente = y3[0]-y3[1]

    for index in range(len(y3)):
        if y3[index]-y3[index+1] != pendiente:
            puntos.append(y3[index])
            pendiente = y3[index]-y3[index+1]
    
    puntos.append(y3[-1])

    puntoOBJ=0
    for punto in puntos:
    
'''

print("Resultados:")
    
def objetivo(y3, yOBJ): # esta función encuentra el conjunto de soluciones optimas y retorna el mejor resultado
    punto = 0           
    diff = 4

    for index in range(len(y3)):            # busca el punto con menor diferencia entre las restricciones
        if y3[index]-yOBJ[index]<diff:      # y la pendiente de la funcion objetivo (cuando esta es trazada con
            diff = y3[index]-yOBJ[index]    # altura (Y) 0=
            punto = y3[index]-yOBJ[index]
            x = index
            y = y3[index]

    return (punto,x,y)  # "punto" corresponde a la altura (Y) que se debe ajustar la función objetivo para que
                        # visiblemente pase por la solución optima


x_vals = np.linspace(0, 4, 1200)    # 120 valores entre 0 y 4
y1 = (3-2.5*x_vals)                 # restricciones
y2 = ((4-x_vals)/2) 
yOBJ = (-0.3*x_vals/0.52)           # funcion objetivo, trazada con altura 0

fig=plt.figure(figsize=(10,8))      # crea la figura

ax = fig.add_subplot(111)

a = b = np.linspace(0, 4, 1000)
X,Y = np.meshgrid(a,b)
Z=0.3*X + 0.52*Y    
cs = ax.contour(X,Y,Z,100, alpha=0.4)   # dibuja las curvas de nivel


plt.plot(x_vals, y1, label=r'$3 \leq 2,5x + y$')    # 2,5x+y >= 3   etiquetas
plt.plot(x_vals, y2, label=r'$4 \leq x + 2y $')     # x+2y >=4 


y3 = np.maximum(y1, y2)        #se define la curva maxima entre y1 e y2

offset, x, y = objetivo(y3, yOBJ)

yOBJ[0:]+= offset

plt.plot(x_vals, yOBJ, label=r'$f(x,y) = 0.3x + 0.52y  $') #  Función objetivo


plt.plot(x_vals[x], y, 'b*', markersize=15) #marca del punto optimo de minimización


# Región factible
plt.fill_between(x_vals, y3, 4, alpha=0.15, color='b')
print("El espacio factible está delimitado por la zona marcada en azul")

plt.axis(ymin = 0)
plt.title('Optimización lineal')
plt.legend()
plt.show()



