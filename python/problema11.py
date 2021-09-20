import matplotlib.pyplot as plt
import numpy as np
import math

cp1 = 2300
m2 = 5
m1 = 3 + 0.75 * m2
cp2 = 4000
Tci = 0
Thi = 50
Th0 = 100
Tc0 = 15
Q = 1000000
n = 0
U = 400
i = 0
n = 4
B = 0
Ap = 0
incre = 2.5

Tci = np.zeros(n + 1);A = np.zeros(n + 1)
for i in range(-1,n):
    Tci[i + 1] = (Q / (m1 * cp1)) + (Tc0)
    print("Tc", i + 1, "= ", Tci[i + 1])
    delT = ((Thi - Tc0) - (Th0 - Tci[i + 1])) / math.log((Thi - Tc0) / (Th0 - Tci[i + 1]))
    print("Delta T",i + 1,"= ",delT)
    A[i + 1] = Q / (U * delT)
    print("A",i + 1,"= ",A[i + 1])
    print()
    B = B + A[i + 1]
    Tc0 = Tc0 + incre
Ap = B / (n + 1)
print("Área promedio= ",Ap)
plt.figure("gráfica de temperaturas")
plt.plot(A,Tci,color="green")
plt.scatter(A,Tci,color="purple")
plt.xlabel("Área de transferencia")
plt.ylabel("Temperatura de entrada")
plt.grid("on")

plt.show()