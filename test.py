import matplotlib.pyplot as plt
import numpy as np


'''def graficar(point1, point2, point3, point4):
    m1_2 = (point2[1]-point1[1])/(point2[0]-point1[0])
    b1_2 = point1[1]

    m3_4 = (point4[1]-point3[1])/(point4[0]-point3[0])
    b3_4 = point3[1]
    #-----------LÍMITES DEL GRAFICO----------
    x = np.linspace(-10,10,500)
    #-----------PUNTO DE INTERSECCIÓN----------
    xi = (b1_2-b3_4) / (m3_4-m1_2)
    yi = m1_2 * xi + b1_2
    print('(xi,yi)',xi,yi)
    #-----------GRAFICO----------
    plt.plot(x,x*m1_2+b1_2)
    plt.plot(x,x*m3_4+b3_4)
    #-----------ATRIBUTOS DEL GRAFICO----------
    plt.grid(linestyle='dotted')
    plt.scatter(xi,yi, color='black' )
    #-----------MOSTRAR RECTAS----------
    plt.show()
'''

#-----------PUNTOS----------
point1 = [np.random.randint(0,6), np.random.randint(0,6)]
point2 = [np.random.randint(1,6), np.random.randint(2,6)]

point3 = [np.random.randint(0,6), np.random.randint(0,6)]
point4 = [np.random.randint(1,6), np.random.randint(2,6)]
#-----------PENDIENTES----------
m12 = (point2[1]-point1[1])/(point2[0]-point1[0])
b12 = point1[1]

m34 = (point4[1]-point3[1])/(point4[0]-point3[0])
b34 = point3[1]
#-----------LÍMITES DEL GRAFICO----------
x = np.linspace(-10,10,500)
#-----------PUNTO DE INTERSECCIÓN----------
xi = (b12-b34) / (m34-m12)
yi = m12 * xi + b12
print('(xi,yi)',xi,yi)
#-----------GRAFICO----------
plt.plot(x,x*m12+b12)
plt.plot(x,x*m34+b34)
#-----------ATRIBUTOS DEL GRAFICO----------
plt.grid(linestyle='dotted')
plt.scatter(xi,yi, color='black' )
#-----------MOSTRAR RECTAS----------
plt.show()