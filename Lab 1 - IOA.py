import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def tryInput(string):
    while(True):
        valor = float(input(string))
        if(isinstance(valor, float)):
            return valor
        else:
            print("Error, ingrese un valor numerico")
    
#funcion que recibe valores de usuario
print("Ingrese coeficientes para X e Y: f(x,y)= [ ]X + [ ]Y")
x0 = float(tryInput("Coeficiente de X: "))
y0 = float(tryInput("Coeficiente de Y: "))

print("Ingrese coeficientes para la restricción 1: [ ]X + [ ]Y <= [ ]")
x1 = float(tryInput("Coeficiente de X: "))
y1 = float(tryInput("Coeficiente de Y: "))
c1 = float(tryInput("Coeficiente C: "))

print("Ingrese coeficientes para la restricción 2: [ ]X + [ ]Y <= [ ]")
x2 = float(tryInput("Coeficiente de X: "))
y2 = float(tryInput("Coeficiente de Y: "))
c2 = float(tryInput("Coeficiente C: "))

print("Ingrese coeficientes para la restricción 3: [ ]X + [ ]Y <= [ ]")
x3 = float(tryInput("Coeficiente de X: "))
y3 = float(tryInput("Coeficiente de Y: "))
c3 = float(tryInput("Coeficiente C: "))

rangoX = int(tryInput("Por favor ingrese los margenes del grafico a visualizar (maximo valor de X e Y): "))


# Parametros iniciales #########
x_vals = np.linspace(0, rangoX, rangoX*300)      
r1 = ((c1-x1*x_vals)/y1)                        
r2 = ((c2-x2*x_vals)/y2) 
r3 = ((c3-x3*x_vals)/y3) 
yOBJ = (-x0*x_vals/y0)          # funcion objetivo, trazada con altura 0
################################


# Curvas de nivel ##############
fig=plt.figure(figsize=(10,8))      # crea la figura

ax = fig.add_subplot(111)

a = b = np.linspace(0, rangoX, 1000)
X,Y = np.meshgrid(a,b)
Z=x0*X + y0*Y    
cs = ax.contour(X,Y,Z,100, alpha=0.4)   
################################


# Etiquetas Restricciones ######
plt.plot(x_vals, r1, label=r'Restricción 1')    # 2,5x+y >= 3   etiquetas
plt.plot(x_vals, r2, label=r'Restricción 2')     # x+2y >=4 
plt.plot(x_vals, r3, label=r'Restricción 3')     # x+2y >=4 

y3 = np.minimum(r1, r2)         #se define la curva minima entre r1 e r2
y3 = np.minimum(y3, r3)         #se define la curva minima entre y3 e r3
################################


# Función objetivo #############
    
def objetivo(y3, yOBJ): # esta función encuentra el conjunto de soluciones optimas y retorna el mejor resultado
    punto = 0           
    diff = 0

    for index in range(len(y3)):            # busca el punto con menor diferencia entre las restricciones
        if y3[index]-yOBJ[index]>diff:      # y la pendiente de la funcion objetivo (cuando esta es trazada con
            diff = y3[index]-yOBJ[index]    # altura (Y) 0=
            punto = y3[index]-yOBJ[index]
            x = index
            y = y3[index]

    return (punto,x,y)  # "punto" corresponde a la altura (Y) que se debe ajustar la función objetivo para que
                        # visiblemente pase por la solución optima

offset, x, y = objetivo(y3, yOBJ)
yOBJ[0:]+= offset           # se ajusta la funcion objetivo para que pase por la solucion optima

plt.plot(x_vals, yOBJ, label=r'Función objetivo') 
################################


plt.plot(x_vals[x], y, 'b*', markersize=15) # marca (estrella) en el punto optimo de maximización


# Región factible #############
plt.fill_between(x_vals, 0, y3, alpha=0.15, color='b')
###############################

print("El espacio factible está delimitado por la zona pintada en azul") #•	Indique si el espacio factible es distinto de vacío (10)

if ((y3[-1]-y3[-2]) > 0):  #se utiliza la pendiente en el ultimo punto de la curva minima para determinar si es abierto o cerrado
    print("El area factible es abierto")    #debido a que todas las restricciones son "menor a", si la pendiente es positiva, es abierta
else:                           
    print("El area factible es cerrada")    #•	Indique si el espacio factible es cerrado o abierto(10)

'''
•	Mostrar gráficamente las curvas de nivel de la función objetivo (5)
•	Mostrar gráficamente, el espacio factible (5)
•	Identificar el conjunto de posibles soluciones del PPL (10)
•	Identificar una solución optima del problema (10)
'''

plt.axis(ymin = 0)
plt.title('Laboratorio 1')
plt.legend()
plt.show()
