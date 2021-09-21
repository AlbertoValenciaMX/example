import matplotlib.pyplot as plt
import numpy as np

x = [[0],[1],[3]] # cm
y = [[0.06],[0.32], [0.6]] # g cm**(-3)
plt.plot(x,y,color="red",label="datos")
plt.grid("on")
# Ajuste lineal
n = 3
xyi = 0
xi = 0
yi = 0
xi2 = 0
# sumatorias necesarias para el método
for i in range(1,n):
    xyi = xyi + (x[i] * y[i])
    xi = xi + x[i]
    yi = yi + y[i]
    xi2 = xi2 + (x[i]**2)

a1 = (n * xyi - xi * yi) / (n * xi2 - xi**2)
xp = xi / n
yp = yi / n
a0 = yp - a1 * xp
print("a0= ",a0," a1= ",a1 )
# Generar la función obtenida y graficarla
f = np.zeros(n)
for i in range(1,n):
    f[i] = a1 * x[i] + a0

plt.plot(x,f,color="green",label="funcion")
plt.leg(bbox_to_anchor=(0.1, 1), loc=2)
# Cálculos adicionales
D = 1.52 * 10**(-6) # cm**2 s**-1
A = 3.6 * 10**(6) # m**2
t = 60 * 20 * 24 * 365 # años
Fm = a1 * D
print("El flujo de masa es aproximadamente ",Fm,"g cm**-2 s**-1")
S = Fm * A * t / 1000
print("Los sedimentos despridos son ",S," kg")

plt.show()