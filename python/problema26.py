import matplotlib.pyplot as plt
import numpy as np

C0 = 3
k = 2
a = 0
b = 60
n = 400
h = (b - a) / n
t = np.zeros(n + 1)
C = np.zeros(n + 1)
C[1] = C0
t[1] = 0
for i in range(1,n):
    fxy = (-k * (C[i]**2))
    C[i + 1] = C[i] + (h * fxy)
    t[i + 1] = t[i] + h
    print("Iteración "+ str(i) + " [C] = "+ str(C[i + 1])+ " en un tiempo de = "+ str(t[i + 1])+ " fxy = "+ str(fxy))

print("La concentración [C]= ",C[n]," mol/L, corresponde cuando pasan ",t[n]," segundos = ", t[n] / 60," minutos ")
plt.figure(1)
plt.plot(t,C,label="Concentración")
plt.scatter(t,C)
plt.xlabel("t Tiempo (seg)")
plt.ylabel("C Concentración (mol/L)")
plt.grid("on")
# plt.leg(bbox_to_anchor=(0.1, 1), loc=2)

plt.show()